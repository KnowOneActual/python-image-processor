import os
from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError
import argparse
import sys

def crop_image(image, aspect_ratio_str):
    """
    Crops an image to a specific aspect ratio from the center.

    Args:
        image (PIL.Image.Image): The image to crop.
        aspect_ratio_str (str): The target aspect ratio as a string (e.g., "16:9", "1:1").

    Returns:
        PIL.Image.Image: The cropped image.
    """
    try:
        ratio_w, ratio_h = map(int, aspect_ratio_str.split(':'))
    except ValueError:
        print(f"Invalid aspect ratio format: '{aspect_ratio_str}'. Use format like '16:9'.")
        return image # Return original image if format is wrong

    img_w, img_h = image.size
    target_ratio = ratio_w / ratio_h

    # Determine the new size of the image that maintains the aspect ratio
    if (img_w / img_h) > target_ratio:
        # Image is wider than the target aspect ratio, crop the width
        new_h = img_h
        new_w = int(new_h * target_ratio)
    else:
        # Image is taller or equal to the target aspect ratio, crop the height
        new_w = img_w
        new_h = int(new_w / target_ratio)

    # Calculate coordinates for a center crop
    left = (img_w - new_w) // 2
    top = (img_h - new_h) // 2
    right = (img_w + new_w) // 2
    bottom = (img_h + new_h) // 2

    return image.crop((left, top, right, bottom))


def add_watermark(image, text, font_size=36, opacity=128):
    """
    Adds a text watermark to an image.
    """
    watermark_image = image.copy().convert("RGBA")
    txt_layer = Image.new("RGBA", watermark_image.size, (255, 255, 255, 0))

    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        print("Arial font not found. Using default font.")
        font = ImageFont.load_default()

    draw = ImageDraw.Draw(txt_layer)
    image_width, image_height = watermark_image.size
    margin = 10
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    position = (image_width - text_width - margin, image_height - text_height - margin)
    draw.text(position, text, font=font, fill=(255, 255, 255, opacity))
    return Image.alpha_composite(watermark_image, txt_layer)


def process_images(input_dir, output_dir, new_width=None, new_format=None, watermark_text=None, crop_ratio=None):
    """
    Resizes, converts, watermarks, and/or crops all images in a directory.
    (Docstring updated to include crop_ratio)
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

                # --- CROPPING ---
                if crop_ratio:
                    processed_img = crop_image(processed_img, crop_ratio)
                    print(f"Cropped '{filename}' to {crop_ratio} aspect ratio")

                # --- RESIZING ---
                if new_width:
                    width, height = processed_img.size
                    aspect_ratio = height / width
                    new_height = int(new_width * aspect_ratio)
                    processed_img = processed_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    print(f"Resized '{filename}' to {new_width}px wide")

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
    parser = argparse.ArgumentParser(description="Bulk resize, convert, watermark, and crop images.")
    parser.add_argument("input_dir", type=str, help="Directory with images to process.")
    parser.add_argument("output_dir", type=str, help="Directory to save processed images.")
    parser.add_argument("--width", type=int, help="New width to resize images to.")
    parser.add_argument("--format", type=str, help="New format (e.g., jpeg, png, webp).")
    parser.add_argument("--watermark", type=str, help="Text to add as a watermark.")
    # --- New Argument for Cropping ---
    parser.add_argument("--crop", type=str, help="Crop to aspect ratio (e.g., '16:9', '1:1').")

    args = parser.parse_args()
    process_images(args.input_dir, args.output_dir, args.width, args.format, args.watermark, args.crop)
