# REAPER Toolbar Icon Creator - Project Summary

## Current State
A production-ready, modular tool for creating professional custom REAPER 3-state toolbar icon strips.

## Key Features
- **State-Based Editor**: Per-state (Default, Hover, Active) control for Background, Border, and Tint.
- **Dynamic Preview**: Real-time zoomable preview with state-persistence.
- **Export System**: Multi-scale (100%, 150%, 200%) PNG export with customizable filenames.
- **Unified UI**: Clean, Dark-themed interface optimized for efficiency.

## Architecture
- **Controller**: `main.py` manages image processing via Pillow and coordinates UI/Logic.
- **View**: Built with PySide6 for a responsive, themeable desktop experience.
- **Controls**: Centralized layout (`controls.py`) for Dimensions, Export, and Style editing.
- **Style Engine**: State-isolated color and border configuration (`style_editor.py`).

