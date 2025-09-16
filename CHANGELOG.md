# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

## [Unreleased]

### Added
- Initial project setup.
