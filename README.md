<p align="center">
<img src="assets/img/python-image-processor_logo.webp" alt="awesome python image processor logo goes here" width="500">
</p>


[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A user-friendly desktop application for bulk image processing. Built with Python and Tkinter, this tool provides both a graphical user interface (GUI) and a command-line interface (CLI) to automate repetitive image tasks.

![Image Processor GUI Screenshot](assets/img/python-image-processor_gui_screenshot_01.webp)

---

## 🚀 Download & Installation (Recommended)

Get the latest standalone application for your operating system. No Python installation required!

1.  Go to the [**Releases Page**](https://github.com/KnowOneActual/python-image-processor/releases).
2.  Download the latest version for your operating system.
3.  Unzip the file and place the application in a convenient location.

### Running the Application

* **Windows:** Double-click the `.exe` file.
* **macOS:**
    1.  Double-click the application. (Dismiss the initial security warning).
    2.  Go to **System Settings** > **Privacy & Security**.
    3.  Scroll down to "Security" and click **"Open Anyway"**.
* **Linux:**
    Most distributions require you to install Tkinter separately if you are running from source.
    ```bash
    sudo apt-get install python3-tk
    ```

---

## ✨ Features

* **Desktop GUI Application**: An intuitive and modern interface.
* **Bulk Processing**: Process entire folders of images at once.
* **Format Conversion**: Convert between `jpeg`, `png`, `webp`, and `gif`.
* **Resizing**: Scale images to a specific width while maintaining aspect ratio.
* **Center Cropping**: Crop images to specific aspect ratios (e.g., `16:9`, `1:1`).
* **Watermarking**: Add customizable text watermarks.
* **Quality Control**: Adjust compression quality for `jpeg` and `webp` files.

---

## 📚 Documentation

We maintain detailed documentation for developers and contributors:

* **[Architecture Overview](docs/Architecture.md)**: Learn how the app handles threading and the image processing pipeline.
* **[Project Roadmap](docs/roadmap.md)**: See what features are planned for future releases.
* **[Contributing Guide](CONTRIBUTING.md)**: Guidelines for submitting PRs and reporting bugs.

---

## 💻 Running from Source

If you want to run the code directly:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/KnowOneActual/python-image-processor.git](https://github.com/KnowOneActual/python-image-processor.git)
    cd python-image-processor
    ```
2.  **Install requirements:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the GUI:**
    ```bash
    python3 app.py
    ```

### Command-Line Usage

For automation, use the CLI:

```bash
python image_processor.py ./input_images ./output_images --crop "1:1" --width 1080 --format jpeg
````

For a full list of commands:

```bash
python image_processor.py --help
```

-----

## ❓ Troubleshooting & FAQ

**Why was my file skipped?**
The processor automatically skips files that are not valid images or have unsupported extensions to prevent crashing. Check the log output for specific error messages.

**The GUI is frozen, what do I do?**
Processing large batches of high-res images can take time. The application uses threading to keep the interface responsive, but if it appears stuck, check your terminal or the internal log window for activity before force-quitting.

**I'm on Linux and the app won't start.**
Ensure you have `python3-tk` installed. See the [Installation](https://www.google.com/search?q=%23download--installation-recommended) section above.

-----

## License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.