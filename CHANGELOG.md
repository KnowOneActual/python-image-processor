# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-11-19

### Added
- **Documentation Site**: Implemented a full documentation website using MkDocs with the Material theme.
- **API Reference**: Added `docs/reference.md` to automatically generate API documentation from code docstrings.
- **Project Documentation**: Added `docs/Architecture.md` and `docs/roadmap.md` to better explain the internal workings and future plans.
- **Contributor Guide**: Created `CONTRIBUTING.md` to outline coding standards (2-space indent) and workflow.

### Changed
- **README Overhaul**: Updated `README.md` with Linux installation tips (`python3-tk`) and a new Troubleshooting/FAQ section.
- **Developer Workflow**: Updated `WARP.md` to include instructions for building and deploying the documentation site.
- **File Organization**: Moved `CONTRIBUTING.md` into the `docs/` directory to integrate with the generated site.


## [1.0.0] - 2025-09-17

### Added
- A full graphical user interface (GUI) in `app.py` using Tkinter.
- The GUI provides access to all image processing features.
- Real-time logging of processing steps within the GUI.
- Threading to keep the GUI responsive during long processing jobs.


## [0.5.0] - 2025-09-17

### Added
- New feature to control compression quality for JPEG and WEBP formats.
- Added a `--quality` command-line argument (1-100) to specify the compression level.

### Changed
- Enhanced the `--help` message to include a section with recommended settings and examples for common use cases.

## [0.4.0] - 2025-09-17

### Added
- New feature to crop images to a specific aspect ratio from the center.
- Added a `--crop` command-line argument that accepts a ratio (e.g., "16:9").

## [0.3.0] - 2025-09-16

### Added
- New feature to add a text watermark to images.
- Added a `--watermark` command-line argument to specify the watermark text.

## [0.2.0] - 2025-09-16

### Changed
- Improved error handling in `image_processor.py`.
- The script now checks if the input directory exists before starting.
- Added specific handling for corrupt or unidentified image files.
- The script now gracefully skips non-image files in the input directory.
- Added logic to handle transparent images (e.g., PNG) when converting to JPEG format.

## [0.1.0] - 2025-09-16

### Added
- Initial project setup.
- Created `image_processor.py` script with core functionality for resizing and converting images.
- Added `README.md` with usage instructions and project roadmap.
- Included `LICENSE`, `CONTRIBUTING.md`, and `.gitignore` files.
- Set up issue templates for bug reports and feature requests.