[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

### ⚠️ Current Status: Work in Progress ⚠️

I'm in the testing stage and should be still considered **unstable**. The basic functions described below may be operational, but features might change, break, or be incomplete.

# Python Image Processor

A user-friendly desktop application for bulk image processing. Built with Python and Tkinter, this tool provides both a graphical user interface (GUI) and a command-line interface (CLI) to automate repetitive image tasks.

![Image Processor GUI Screenshot](docs/gui-screenshot.jpg)

---

## ✨ Features

This tool is packed with features to make your image workflow faster and more efficient:

* **Desktop GUI Application**: An intuitive and modern interface that's easy for anyone to use.
* **Bulk Processing**: Process entire folders of images at once.
* **Format Conversion**: Convert between `jpeg`, `png`, `webp`, and `gif`.
* **Resizing**: Scale images to a specific width while maintaining the aspect ratio.
* **Center Cropping**: Crop images to a specific aspect ratio (e.g., `16:9`, `1:1`).
* **Watermarking**: Add a customizable text watermark to your images.
* **Quality Control**: Adjust the compression quality for `jpeg` and `webp` files to balance file size and quality.
* **Responsive UI**: The application remains responsive even when processing large batches of images, thanks to multi-threading.

---

## 🚀 Getting Started

There are two ways to use the Python Image Processor: by downloading the standalone application or by running the source code directly.

### 1. Download the Standalone App (Recommended)

For most users, this is the easiest way to get started.

1.  Go to the [**Releases Page**](https://github.com/KnowOneActual/python-image-processor/releases) for this repository.
2.  Download the latest version for your operating system (e.g., the `.zip` or `.dmg` file for macOS, `.exe` for Windows).
3.  Unzip the file and run the application.

### 2. Run from Source

If you are a developer and want to run the code directly, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/KnowOneActual/python-image-processor.git](https://github.com/KnowOneActual/python-image-processor.git)
    cd python-image-processor
    ```
2.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    pip install sv_ttk
    ```
3.  **Run the GUI application:**
    ```bash
    python3 app.py
    ```

---

## 💻 Command-Line Usage

For automation and power users, the CLI provides access to all processing features.

**Basic Structure:**
```bash
python image_processor.py <input_dir> <output_dir> [options]
````

**Common Examples:**

  * **For Web Use (Good balance of size and quality):**
    ```bash
    python image_processor.py ./input_images ./output_images --format webp --quality 75
    ```
  * **For Social Media (Square Post, e.g., Instagram):**
    ```bash
    python image_processor.py ./input_images ./output_images --crop "1:1" --width 1080 --format jpeg
    ```
  * **To Create Small Thumbnails:**
    ```bash
    python image_processor.py ./input_images ./output_images --width 150 --format jpeg --quality 65
    ```

For a full list of commands and options, run:

```bash
python image_processor.py --help
```

-----

## 🛣️ Roadmap

This project is actively maintained. Future enhancements may include:

  * Adding more advanced filename options (e.g., adding a prefix or suffix).
  * Implementing a comprehensive test suite with pytest.
  * Support for additional image effects (e.g., brightness, contrast).
 
 Please feel free to open an issue or submit a pull request.
