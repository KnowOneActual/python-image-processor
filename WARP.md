# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a Python-based image processing tool that provides bulk image processing capabilities including resizing, format conversion, and watermarking. The project uses PIL/Pillow for image manipulation.

### Key Features
- **Bulk image processing**: Process entire directories of images
- **Cropping**: Crop images to specific aspect ratios (16:9, 1:1, etc.) from center
- **Resizing**: Resize images while maintaining aspect ratio
- **Format conversion**: Convert between common image formats (PNG, JPEG, WebP, etc.)
- **Compression quality control**: Adjustable quality settings for JPEG and WebP formats (1-100)
- **Watermarking**: Add text watermarks with customizable opacity and positioning
- **Error handling**: Robust handling of corrupt or invalid image files

## Development Workflow

### Starting New Work
Use the provided Git workflow script:
```bash
./start-work.sh
```
This script:
1. Checks for uncommitted changes
2. Prompts for a new branch name
3. Syncs the main branch with remote
4. Creates and switches to the new feature branch

### Branch Management
- Main branch: `main`
- Follow conventional branch naming (e.g., `feature/add-user-login`, `bugfix/memory-leak`)
- Always start new work from an updated main branch

## Project Structure

- `image_processor.py` - Main image processing module with cropping, resizing, watermarking, and batch processing
- `requirements.txt` - Python dependencies (Pillow)
- `input_images/` - Sample input directory for testing
- `output_images/` - Default output directory for processed images
- `.venv/` - Python virtual environment (git-ignored)
- `src/` - Source code directory (legacy, contains empty `main` file)
- `tests/` - Test directory (currently empty)
- `docs/` - Documentation directory (contains empty `index.md`)
- `.github/ISSUE_TEMPLATE/` - GitHub issue templates for bugs and features

## Code Standards

### Editor Configuration
The project uses `.editorconfig` with the following standards:
- **Indentation**: 2 spaces for all files
- **Line endings**: LF (Unix-style)
- **Charset**: UTF-8
- **Trailing whitespace**: Trimmed
- **Final newline**: Required

### Git Workflow
- Clean working directory required before starting new features
- Pull latest changes from `origin/main` before branching
- Use descriptive branch names following the pattern shown in `start-work.sh`

## Development Commands

### Environment Setup
```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### Running the Image Processor
```bash
# Basic usage
python image_processor.py input_folder output_folder

# Crop images to square (1:1 aspect ratio)
python image_processor.py input_images output_images --crop "1:1"

# Crop to widescreen and resize
python image_processor.py input_images output_images --crop "16:9" --width 1280

# Resize images to 800px width
python image_processor.py input_folder output_folder --width 800

# Convert all images to JPEG with custom quality
python image_processor.py input_folder output_folder --format jpeg --quality 85

# Web optimization (WebP format with balanced quality)
python image_processor.py input_folder output_folder --format webp --quality 75

# Add watermark
python image_processor.py input_folder output_folder --watermark "© 2024 My Company"

# Combine all operations (crop, resize, convert, compress, watermark)
python image_processor.py input_images output_images --crop "16:9" --width 800 --format jpeg --quality 85 --watermark "© 2024"

# Social media ready (Instagram square posts)
python image_processor.py input_images output_images --crop "1:1" --width 1080 --format jpeg --quality 90

# Small thumbnails with high compression
python image_processor.py input_images output_images --width 150 --format jpeg --quality 65
```

### Development Tasks
```bash
# Deactivate virtual environment
deactivate

# Add new dependencies
pip install package_name
pip freeze > requirements.txt
```

## Architecture Overview

### Core Functions
- **`crop_image()`**: Crops images to specific aspect ratios (e.g., 16:9, 1:1) from the center
- **`add_watermark()`**: Applies transparent text watermarks to images with customizable font size and opacity
- **`process_images()`**: Main batch processing function that handles cropping, resizing, format conversion, compression, and watermarking
- **Error handling**: Graceful handling of corrupt images and invalid file types

### Image Processing Pipeline
1. **Input validation**: Checks directory existence and file types
2. **Image loading**: Uses PIL to open and validate images
3. **Processing**: Applies transformations in order (crop → resize → watermark → format conversion with compression)
4. **Output**: Saves processed images to specified directory with optimized quality settings

### Supported Formats
- **Input**: PNG, JPEG, GIF, BMP, WebP
- **Output**: All Pillow-supported formats with automatic RGBA→RGB conversion for JPEG

## Development Notes

### Current State
- ✅ Core image processing functionality implemented (cropping, resizing, watermarking, format conversion)
- ✅ Compression quality control for JPEG and WebP formats (v0.5.0)
- ✅ Enhanced help documentation with usage examples and recommended settings
- ✅ Virtual environment and dependency management setup
- ✅ Command-line interface with argparse
- ✅ Error handling and file validation
- ✅ Sample input/output directories for testing
- ✅ Version tracking with CHANGELOG.md
- 🔄 No testing framework configured yet
- 🔄 No CI/CD pipeline setup
- 🔄 Code formatting/linting tools not configured

### Future Enhancements
- Add comprehensive test suite (pytest)
- Implement logging instead of print statements
- Add progress bars for batch processing
- Support for additional image effects (blur, brightness, contrast)
- Configuration file support
- GUI interface option
- Batch optimization targeting specific file sizes
- Advanced filename options (prefixes/suffixes, custom naming patterns)

### Git Configuration
The `.gitignore` includes comprehensive exclusions for:
- Python bytecode and virtual environments
- OS-specific files (macOS .DS_Store, Windows Thumbs.db)
- Editor/IDE configurations
- Build and distribution artifacts
- Environment variables and secrets
- Personal scratch files and shortcuts