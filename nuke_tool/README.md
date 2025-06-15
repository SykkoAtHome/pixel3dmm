# Pixel3DMM Nuke Integration

This directory contains a minimal wrapper for running the Pixel3DMM pipeline directly inside The Foundry Nuke.
It exposes a small UI and helper functions to launch preprocessing, inference and tracking.

## Installation
1. Copy the entire repository (or at least the `nuke_tool`, `src` and `scripts` directories) to a location included in your Nuke plugin path or add the repository root to `NUKE_PATH`.
2. The module automatically extends `sys.path` so the `pixel3dmm` package and scripts can be imported.
3. Ensure environment variables defined in `env_paths.py` are configured either via `~/.config/pixel3dmm/.env` or by editing the file directly.

## Usage
In Nuke's Python console run:
```python
import nuke_tool.menu as pm
pm.add_menu()
```
This adds a **Pixel3DMM** entry to the main menu which opens a simple panel for selecting a video or image sequence.

Running the pipeline will create the preprocessing and tracking results in the locations specified by the environment variables.
