import os
from PIL import Image, UnidentifiedImageError
import argparse
import sys

def process_images(input_dir, output_dir, new_width=None, new_format=None):
    """
    Resizes and/or converts all images in a directory.

    Args:
        input_dir (str): The directory containing the original images.
        output_dir (str): The directory where processed images will be saved.
        new_width (int, optional): The new width for the images. Height is scaled automatically.
        new_format (str, optional): The new format for the images (e.g., 'jpeg', 'png', 'webp').
    """
    # --- 1. Check if the input directory exists ---
    if not os.path.isdir(input_dir):
        print(f"Error: Input directory '{input_dir}' not found.")
        sys.exit(1) # Exit the script if the input directory doesn't exist

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    # Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)

        # --- 2. Skip subdirectories and non-image files ---
        valid_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')
        if not os.path.isfile(input_path) or not filename.lower().endswith(valid_extensions):
            print(f"Skipped: '{filename}' is not a recognized image file.")
            continue

        try:
            with Image.open(input_path) as img:
                processed_img = img.copy() # Work on a copy to avoid issues

                # --- RESIZING ---
                if new_width:
                    width, height = processed_img.size
                    aspect_ratio = height / width
                    new_height = int(new_width * aspect_ratio)
                    processed_img = processed_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    print(f"Resized '{filename}' to {new_width}x{new_height}")

                # --- CONVERSION ---
                output_filename = filename
                if new_format:
                    base_filename, _ = os.path.splitext(filename)
                    output_filename = f"{base_filename}.{new_format.lower()}"

                output_path = os.path.join(output_dir, output_filename)

                # Convert to RGB if saving as JPEG to avoid errors with transparent images
                if new_format and new_format.lower() in ['jpeg', 'jpg']:
                    if processed_img.mode in ("RGBA", "P"):
                        processed_img = processed_img.convert("RGB")

                processed_img.save(output_path)
                print(f"Saved processed image to '{output_path}'")

        # --- 3. More specific error handling ---
        except UnidentifiedImageError:
            print(f"Could not process '{filename}'. It may be corrupt or not a valid image file.")
        except Exception as e:
            print(f"An unexpected error occurred with '{filename}': {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bulk resize and convert images.")
    parser.add_argument("input_dir", type=str, help="Directory with images to process.")
    parser.add_argument("output_dir", type=str, help="Directory to save processed images.")
    parser.add_argument("--width", type=int, help="New width to resize images to.")
    parser.add_argument("--format", type=str, help="New format to convert images to (e.g., jpeg, png, webp).")

    args = parser.parse_args()
    process_images(args.input_dir, args.output_dir, args.width, args.format)
