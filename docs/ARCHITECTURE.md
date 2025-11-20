## Architecture Overview

### GUI Application (`app.py`)
- **`ImageProcessorApp`**: Main Tkinter application class with modern dark theme (sv_ttk)
- **Folder selection**: Browse for input and output directories
- **Processing options**: Checkboxes and controls for all image processing features
- **Real-time logging**: Text widget displays processing progress and status
- **Threading**: Prevents UI freezing during long operations
- **Progress indication**: Progress bar shows processing status

### Core Processing Functions (`image_processor.py`)
- **`crop_image()`**: Crops images to specific aspect ratios (e.g., 16:9, 1:1) from the center
- **`add_watermark()`**: Applies transparent text watermarks to images with customizable font size and opacity
- **`process_images()`**: Main batch processing function that handles cropping, resizing, format conversion, compression, and watermarking
- **Logger parameter**: Supports both CLI (print) and GUI (custom logger) output
- **Error handling**: Graceful handling of corrupt images and invalid file types

### Image Processing Pipeline
1. **Input validation**: Checks directory existence and file types
2. **Image loading**: Uses PIL to open and validate images
3. **Processing**: Applies transformations in order (crop → resize → watermark → format conversion with compression)
4. **Output**: Saves processed images to specified directory with optimized quality settings

### Supported Formats
- **Input**: PNG, JPEG, GIF, BMP, WebP
- **Output**: All Pillow-supported formats with automatic RGBA→RGB conversion for JPEG