[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

### ⚠️ Current Status: Work in Progress ⚠️

I'm in the early stages of development and should be considered **unstable**. The basic functions described below may be operational, but features might change, break, or be incomplete.


# Python Image Processor

A command-line tool built with Python to bulk resize, convert, watermark, and crop images. This script is designed to automate the repetitive task of preparing images for web use or archiving.

## What is this?

This project is a simple yet powerful Python script that allows you to process an entire folder of images at once. You can resize images to a specific width, convert them to different file formats, add a text watermark, and **crop them to a specific aspect ratio**.

## Why was this created?

Manually processing images one by one is time-consuming and inefficient. This tool was created to solve that problem by providing a fast, automated way to handle these tasks. It serves as a practical utility for web developers, content creators, or anyone who frequently works with large batches of images. It's also a project to demonstrate skills in Python, command-line interface (CLI) development, and image manipulation using the Pillow library.

## How to Use

### Prerequisites

* Python 3.6+
* Pillow library

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/KnowOneActual/python-image-processor.git](https://github.com/KnowOneActual/python-image-processor.git)
    cd python-image-processor
    ```

2.  **Install the required library:**
    ```bash
    pip install Pillow
    ```

### Usage

The script is run from the command line and takes an input directory and an output directory as required arguments.

**Basic Structure:**
```bash
python image_processor.py <input_directory> <output_directory> [--width <number>] [--format <type>] [--watermark "<text>"] [--crop "<w:h>"]
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

  * **To combine resizing, converting, and watermarking:**

    ```bash
    python image_processor.py ./input_images ./output_images --width 300 --format jpeg --watermark "DRAFT"
    ```

## Roadmap

This is an active project with plans for future enhancements. Here are some features I'm considering for upcoming versions:

  * **Graphical User Interface (GUI):** Develop a simple GUI using a library like Tkinter or PyQt to make the tool accessible to non-technical users.
  * **Add More Features:**
      * Introduce image compression options to target a specific file size.
      * Add advanced filename options (e.g., adding a suffix).
  * **Enhanced Error Handling:** Continue to improve validation and user feedback.