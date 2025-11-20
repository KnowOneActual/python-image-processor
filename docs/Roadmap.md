# Project Roadmap

This document outlines the current status of the project and planned features for future releases.

## ✅ Completed Features

**Version 1.1.0 (Documentation Update)**
- [x] Full documentation site with MkDocs.
- [x] Contributing guidelines and architectural overview.

**Version 1.0.0 (Initial Release)**
- [x] Desktop GUI with dark mode (sv_ttk).
- [x] Bulk processing (entire folders).
- [x] Smart center-cropping (1:1, 16:9).
- [x] Format conversion (JPEG, PNG, WebP).
- [x] Adjustable compression quality.
- [x] Watermarking support.

## 🚀 Future Enhancements

These are the prioritized features we plan to work on next.

### Short Term
- [X] **Test Suite**: Implement `pytest` to ensure image processing logic is robust and regression-free.
- [ ] **Configuration Files**: Allow saving/loading user presets (e.g., "Instagram Settings" or "Web Optimization").
- [ ] **Structured Logging**: Replace `print` statements in the CLI with a proper Python `logging` configuration.

### Medium Term
- [ ] **Drag-and-Drop**: Allow users to drag files directly into the GUI window.
- [ ] **Image Effects**: Add basic filters like Brightness, Contrast, and Saturation.
- [ ] **Advanced Filenaming**: Add support for prefixes, suffixes, and custom naming patterns (e.g., `img_001_processed.jpg`).

### Long Term
- [ ] **Plugin System**: Allow 3rd party developers to write custom effect scripts.
- [ ] **Multi-threading**: Process multiple images in parallel (currently one by one in a background thread).

 
 Please feel free to open an issue or submit a pull request.
