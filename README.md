[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

### ⚠️ Current Status: Work in Progress ⚠️

I'm in the testing stage and should be still considered **unstable**. The basic functions described below may be operational, but features might change, break, or be incomplete.

# Python Image Processor

A command-line tool and desktop application built with Python to bulk resize, convert, watermark, and crop images. This script is designed to automate the repetitive task of preparing images for web use or archiving.

## Desktop GUI Application

This project also includes a user-friendly desktop application built with Tkinter.

![Image Processor GUI Screenshot](docs/gui-screenshot.jpg)

### How to Use the GUI

1.  **Prerequisites:** Ensure you have Python 3.6+ and the required libraries installed.
    ```bash
    pip install Pillow sv_ttk
    ```
2.  **Run the App:** Navigate to the project directory and run the following command:
    ```bash
    python3 app.py
    ```
3.  **Usage:**
    * Use the buttons to select your input and output folders.
    * Select the checkboxes for the operations you want to perform and fill in the options.
    * Click the "Start Processing" button. Progress will be shown in the log window.

## Command-Line Interface (CLI)

For advanced users and automation, the powerful command-line tool is still available.

### How to Use the CLI

**Basic Structure:**
```bash
python image_processor.py <input_directory> <output_directory> [--width <number>] [--format <type>] [--watermark "<text>"] [--crop "<w:h>"] [--quality <number>]
````

**Examples:**

  * **To crop all images to a square (1:1 aspect ratio):**

    ```bash
    python image_processor.py ./input_images ./output_images --crop "1:1"
    ```

  * **To crop images to 16:9 and then resize them to 1280px wide:**

    ```bash
    python image_processor.py ./input_images ./output_images --crop "16:9" --width 1280
    ```

## Roadmap

This is an active project with plans for future enhancements. Here are some features I'm considering for upcoming versions:

  * **Add More Features:**
      * Add advanced filename options (e.g., adding a suffix).
  * **Enhanced Error Handling:** Continue to improve validation and user feedback.