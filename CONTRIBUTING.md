# Contributing to Python Image Processor

First off, thank you for considering contributing to Python Image Processor! It's people like you that make the open-source community such an amazing place to learn, inspire, and create.

## How Can I Contribute?

### Reporting Bugs
This project uses GitHub Issues to track bugs. If you find a bug, please [open a new issue](https://github.com/KnowOneActual/python-image-processor/issues/new). We have a Bug Report template ready for you to fill out.

### Suggesting Enhancements
If you have an idea for a new feature or an improvement to an existing one, please submit a Feature Request using our [issue template](https://github.com/KnowOneActual/python-image-processor/issues/new).

### Pull Requests
1.  **Fork the repository** and clone it locally.
2.  **Create a branch** for your edits. Please use a descriptive name for your branch (e.g., `feature/add-user-login` or `bugfix/memory-leak`).
3.  **Make your changes** in your local branch.
4.  **Submit a Pull Request** to the `main` branch.

## Development Setup

If you want to run the code locally to test changes, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/KnowOneActual/python-image-processor.git
    cd python-image-processor
    ```

2.  **Set up your environment:**
    We recommend using a virtual environment to manage dependencies.
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    * **GUI:** `python app.py`
    * **CLI:** `python image_processor.py --help`

## Project Structure

To help you navigate the codebase:
* `app.py`: The main desktop GUI application (Tkinter).
* `image_processor.py`: The core processing logic (cropping, resizing, watermarking).
* `input_images/`: Use this directory for testing your input files.
* `output_images/`: The default location for processed files.

## Coding Standards

Please adhere to the following standards to keep the codebase consistent:

* **Indentation:** Use **2 spaces** for all files (Python, Markdown, etc.).
* **Line Endings:** Use Unix-style (LF) line endings.
* **Encoding:** UTF-8.
* **Imports:** Keep imports organized at the top of the file.

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
