## Project Overview

This is a Python-based image processing tool that provides bulk image processing capabilities including resizing, format conversion, and watermarking. The project offers both a command-line interface (CLI) and a desktop GUI application built with Tkinter. The project uses PIL/Pillow for image manipulation.

### Key Features
- **Desktop GUI Application**: User-friendly Tkinter interface with real-time logging and threading
- **Command-line Interface**: Powerful CLI tool for automation and advanced users
- **Bulk image processing**: Process entire directories of images
- **Cropping**: Crop images to specific aspect ratios (16:9, 1:1, etc.) from center
- **Resizing**: Resize images while maintaining aspect ratio
- **Format conversion**: Convert between common image formats (PNG, JPEG, WebP, etc.)
- **Compression quality control**: Adjustable quality settings for JPEG and WebP formats (1-100)
- **Watermarking**: Add text watermarks with customizable opacity and positioning
- **Error handling**: Robust handling of corrupt or invalid image files
- **Responsive UI**: Threading keeps the GUI responsive during long processing jobs

## Development Workflow

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
- `app.py` - Desktop GUI application built with Tkinter
- `requirements.txt` - Python dependencies (Pillow, sv_ttk)
- `input_images/` - Sample input directory for testing
- `output_images/` - Default output directory for processed images
- `.venv/` - Python virtual environment (git-ignored)
- `src/` - Source code directory (legacy, contains empty `main` file)
- `tests/` - Test directory (currently empty)
- `docs/` - Documentation directory (contains GUI screenshot and empty `index.md`)
- `.github/ISSUE_TEMPLATE/` - GitHub issue templates for bugs and features
- `CHANGELOG.md` - Version history and feature additions
- `app.spec` - PyInstaller specification file (for building executable)
- `docs/gui-screenshot.jpg` - Screenshot of the GUI application

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
- Use descriptive branch names