import os
from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError
import argparse
import sys

def add_watermark(image, text, font_size=36, opacity=128):
    """
    Adds a text watermark to an image.

    Args:
        image (PIL.Image.Image): The image to add the watermark to.
        text (str): The watermark text.
        font_size (int): The size of the font.
        opacity (int): The opacity of the text (0-255).

    Returns:
        PIL.Image.Image: The image with the watermark.
    """
    # Make a copy of the image to work with
    watermark_image = image.copy().convert("RGBA")

    # Create a transparent layer for the text
    txt_layer = Image.new("RGBA", watermark_image.size, (255, 255, 255, 0))

    # Select a font
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        print("Arial font not found. Using default font.")
        font = ImageFont.load_default()

    # Get a drawing context
    draw = ImageDraw.Draw(txt_layer)

    # Calculate text position (bottom right corner with a margin)
    image_width, image_height = watermark_image.size
    margin = 10
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    position = (image_width - text_width - margin, image_height - text_height - margin)

    # Add the text to the transparent layer
    draw.text(position, text, font=font, fill=(255, 255, 255, opacity))

    # Composite the text layer onto the original image
    return Image.alpha_composite(watermark_image, txt_layer)


def process_images(input_dir, output_dir, new_width=None, new_format=None, watermark_text=None):
    """
    Resizes, converts, and/or watermarks all images in a directory.
    (Docstring updated to include watermark_text)
    """
    if not os.path.isdir(input_dir):
        print(f"Error: Input directory '{input_dir}' not found.")
        sys.exit(1)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)

        valid_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')
        if not os.path.isfile(input_path) or not filename.lower().endswith(valid_extensions):
            print(f"Skipped: '{filename}' is not a recognized image file.")
            continue

        try:
            with Image.open(input_path) as img:
                processed_img = img.copy()

                if new_width:
                    width, height = processed_img.size
                    aspect_ratio = height / width
                    new_height = int(new_width * aspect_ratio)
                    processed_img = processed_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    print(f"Resized '{filename}' to {new_width}x{new_height}")

                # --- WATERMARKING ---
                if watermark_text:
                    processed_img = add_watermark(processed_img, watermark_text)
                    print(f"Added watermark to '{filename}'")

                output_filename = filename
                if new_format:
                    base_filename, _ = os.path.splitext(filename)
                    output_filename = f"{base_filename}.{new_format.lower()}"

                output_path = os.path.join(output_dir, output_filename)

                if new_format and new_format.lower() in ['jpeg', 'jpg']:
                    if processed_img.mode in ("RGBA", "P"):
                        processed_img = processed_img.convert("RGB")

                processed_img.save(output_path)
                print(f"Saved processed image to '{output_path}'")

        except UnidentifiedImageError:
            print(f"Could not process '{filename}'. It may be corrupt or not a valid image file.")
        except Exception as e:
            print(f"An unexpected error occurred with '{filename}': {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bulk resize, convert, and watermark images.")
    parser.add_argument("input_dir", type=str, help="Directory with images to process.")
    parser.add_argument("output_dir", type=str, help="Directory to save processed images.")
    parser.add_argument("--width", type=int, help="New width to resize images to.")
    parser.add_argument("--format", type=str, help="New format to convert images to (e.g., jpeg, png, webp).")
    # --- New Argument for Watermark ---
    parser.add_argument("--watermark", type=str, help="Text to add as a watermark.")

    args = parser.parse_args()
    process_images(args.input_dir, args.output_dir, args.width, args.format, args.watermark)
