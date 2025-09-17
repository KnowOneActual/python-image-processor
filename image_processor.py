import os
from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError
import argparse
import sys

def crop_image(image, aspect_ratio_str):
    """
    Crops an image to a specific aspect ratio from the center.
    """
    try:
        ratio_w, ratio_h = map(int, aspect_ratio_str.split(':'))
    except ValueError:
        print(f"Invalid aspect ratio format: '{aspect_ratio_str}'. Use format like '16:9'.")
        return image

    img_w, img_h = image.size
    target_ratio = ratio_w / ratio_h

    if (img_w / img_h) > target_ratio:
        new_h = img_h
        new_w = int(new_h * target_ratio)
    else:
        new_w = img_w
        new_h = int(new_w / target_ratio)

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


def process_images(input_dir, output_dir, new_width=None, new_format=None, watermark_text=None, crop_ratio=None, quality=95):
    """
    Resizes, converts, watermarks, crops, and compresses all images in a directory.
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

                if crop_ratio:
                    processed_img = crop_image(processed_img, crop_ratio)
                    print(f"Cropped '{filename}' to {crop_ratio} aspect ratio")

                if new_width:
                    width, height = processed_img.size
                    aspect_ratio = height / width
                    new_height = int(new_width * aspect_ratio)
                    processed_img = processed_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    print(f"Resized '{filename}' to {new_width}px wide")

                if watermark_text:
                    processed_img = add_watermark(processed_img, watermark_text)
                    print(f"Added watermark to '{filename}'")

                output_filename = filename
                current_format = new_format if new_format else os.path.splitext(filename)[1][1:].lower()

                if new_format:
                    base_filename, _ = os.path.splitext(filename)
                    output_filename = f"{base_filename}.{new_format.lower()}"

                output_path = os.path.join(output_dir, output_filename)

                save_options = {}
                if current_format in ['jpeg', 'jpg', 'webp']:
                    save_options['quality'] = quality
                    print(f"Set quality for '{filename}' to {quality}")

                if current_format in ['jpeg', 'jpg']:
                    if processed_img.mode in ("RGBA", "P"):
                        processed_img = processed_img.convert("RGB")

                processed_img.save(output_path, **save_options)
                print(f"Saved processed image to '{output_path}'")

        except UnidentifiedImageError:
            print(f"Could not process '{filename}'. It may be corrupt or not a valid image file.")
        except Exception as e:
            print(f"An unexpected error occurred with '{filename}': {e}")

if __name__ == "__main__":
    # --- Help text with usage examples (epilog) ---
    help_examples = """
    Recommended Settings & Examples:
    --------------------------------

    1. For Web Use (Good balance of size and quality):
       python image_processor.py <in_dir> <out_dir> --format webp --quality 75

    2. For Social Media (Square Post, e.g., Instagram):
       python image_processor.py <in_dir> <out_dir> --crop "1:1" --width 1080 --format jpeg

    3. To Create Small Thumbnails:
       python image_processor.py <in_dir> <out_dir> --width 150 --format jpeg --quality 65

    4. To Add a Copyright Watermark:
       python image_processor.py <in_dir> <out_dir> --watermark "© 2025 Your Name"
    """

    # --- Argument Parser Setup ---
    parser = argparse.ArgumentParser(
        description="Bulk resize, convert, watermark, crop, and compress images.",
        epilog=help_examples,
        formatter_class=argparse.RawDescriptionHelpFormatter # Allows for multi-line epilog
    )

    parser.add_argument("input_dir", type=str, help="Directory with images to process.")
    parser.add_argument("output_dir", type=str, help="Directory to save processed images.")
    parser.add_argument("--width", type=int, help="New width to resize images to.")
    parser.add_argument("--format", type=str, help="New format (e.g., jpeg, png, webp).")
    parser.add_argument("--watermark", type=str, help="Text to add as a watermark.")
    parser.add_argument("--crop", type=str, help="Crop to aspect ratio (e.g., '16:9', '1:1').")
    parser.add_argument("--quality", type=int, default=95, help="Compression quality for JPEG/WEBP (1-100, default: 95).")

    args = parser.parse_args()
    process_images(args.input_dir, args.output_dir, args.width, args.format, args.watermark, args.crop, args.quality)
