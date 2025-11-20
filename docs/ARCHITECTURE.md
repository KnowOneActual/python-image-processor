# Architecture Overview

This document provides a high-level overview of the Python Image Processor's internal design and component structure.

## System Components

### 1. GUI Application (`app.py`)
The user interface is built using **Tkinter** with the **Sun Valley (sv_ttk)** theme for a modern dark mode aesthetic.

* **`ImageProcessorApp` Class**: The main entry point. It inherits from `tk.Tk` and manages the entire lifecycle of the application.
* **Threading Model**: To prevent the UI from freezing during heavy image processing tasks, the app spawns a separate `threading.Thread` for the `process_images` function.
* **Event Loop**: The main Tkinter event loop handles user inputs (clicks, folder selection) while the background thread updates the UI via a thread-safe logging mechanism.

### 2. Core Processing Logic (`image_processor.py`)
This module is decoupled from the GUI, allowing it to be used as a CLI tool or imported as a library.

* **Dependency**: Heavily relies on **PIL (Pillow)** for all image manipulations.
* **Key Functions**:
    * `crop_image()`: Calculates center-based cropping coordinates to fit specific aspect ratios (e.g., 16:9).
    * `add_watermark()`: Creates a transparent text layer and composites it over the original image.
    * `process_images()`: The orchestrator function that iterates through files and applies transformations in a specific order.

## Image Processing Pipeline

When a batch job is started, each image goes through the following transformation pipeline:

1.  **Input Validation**: Checks if the file is a valid image (PNG, JPEG, BMP, WebP, etc.).
2.  **Cropping (Optional)**: If enabled, crops the image from the center to the target aspect ratio.
3.  **Resizing (Optional)**: Scales the image to the target width using `Image.Resampling.LANCZOS` for high quality.
4.  **Watermarking (Optional)**: Applies the text watermark with customizable opacity.
5.  **Format Conversion**: Converts the image to the target format (e.g., RGBA to RGB for JPEG).
6.  **Compression**: Saves the final file with the specified quality setting (1-100).