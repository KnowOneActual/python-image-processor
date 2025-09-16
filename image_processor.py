import os
from PIL import Image
import argparse

def process_images(input_dir, output_dir, new_width=None, new_format=None):
    """
    Resizes and/or converts all images in a directory.

    Args:
        input_dir (str): The directory containing the original images.
        output_dir (str): The directory where processed images will be saved.
        new_width (int, optional): The new width for the images. Height is scaled automatically.
        new_format (str, optional): The new format for the images (e.g., 'jpeg', 'png', 'webp').
    """
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    # Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        # Construct the full file path
        input_path = os.path.join(input_dir, filename)

        # Check if it's a file and not a directory
        if os.path.isfile(input_path):
            try:
                with Image.open(input_path) as img:
                    # --- RESIZING ---
                    if new_width:
                        # Calculate the new height to maintain aspect ratio
                        width, height = img.size
                        aspect_ratio = height / width
                        new_height = int(new_width * aspect_ratio)
                        # Resize the image
                        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                        print(f"Resized {filename} to {new_width}x{new_height}")

                    # --- CONVERSION ---
                    output_filename = filename
                    if new_format:
                        # Change the file extension
                        base_filename, _ = os.path.splitext(filename)
                        output_filename = f"{base_filename}.{new_format.lower()}"

                    # Construct the output path
                    output_path = os.path.join(output_dir, output_filename)

                    # Save the processed image
                    # The format is inferred from the file extension
                    img.save(output_path)
                    print(f"Saved processed image to {output_path}")

            except Exception as e:
                print(f"Could not process {filename}. Reason: {e}")

if __name__ == "__main__":
    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(description="Bulk resize and convert images.")

    parser.add_argument("input_dir", type=str, help="Directory with images to process.")
    parser.add_argument("output_dir", type=str, help="Directory to save processed images.")
    parser.add_argument("--width", type=int, help="New width to resize images to.")
    parser.add_argument("--format", type=str, help="New format to convert images to (e.g., jpeg, png, webp).")

    args = parser.parse_args()

    # Call the main function with the provided arguments
    process_images(args.input_dir, args.output_dir, args.width, args.format)
