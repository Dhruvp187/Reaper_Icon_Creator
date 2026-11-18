# REAPER Toolbar Icon Creator

A modular, professional-grade tool for creating custom 3-state (Default, Hover, Active) toolbar icon strips for REAPER.

## Features
- **State-Based Design**: Separate style configuration for Default, Hover, and Active icon states.
- **Style Controls**: Customize Background colors, Border (thickness/radius), and Tint intensity/color for each state.
- **Flexible Dimensions**: Live preview and re-sizing for icons.
- **Export**: Batch export icon strips at multiple scales (100%, 150%, 200%).
- **Modern UI**: Dark-themed, efficient interface built with PySide6.

## Installation
1. Clone the repository: `git clone [url]`
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python -m src.main`

## Project Structure
- `src/main.py`: Controller logic & Image processing (Pillow).
- `src/ui.py`: Main application window & Styling (PySide6).
- `src/controls.py`: Unified control panel and sidebar layout.
- `src/style_editor.py`: Component for editing per-state icon styles.
- `src/preview.py`: Zoomable, persistent-state image viewer.

## Building Executables
This project is structured for easy packaging using PyInstaller.
1. Install PyInstaller: `pip install pyinstaller`
2. Build command: `pyinstaller --onefile --windowed src/main.py`
