# Visual Studio Code Configuration

This guide explains how to configure VS Code for optimal Python development using the provided workspace configuration file.

- [Introduction](#introduction)
- [Installing Extensions](#installing-extensions)
- [Workspace Configuration](#workspace-configuration)

## Introduction

The workspace configuration file `.vscode/settings.json` is automatically used when the workspace is opened. It includes both global and Python-specific settings. Global settings can be moved to the user settings file if needed. To do this:

- Press `Ctrl + Shift + P`.
- Type `Preferences: Open User Settings (JSON)` and press Enter.

## Installing Extensions

To install any necessary extensions:

1. Open the "Extensions" tab (`Ctrl/Cmd + Shift + X`).
2. Search for the extensions by name.
3. Install and enable them by workspace to minimize performance degradation. This can be achieved by selecting a disabled extension and choosing "Enable (Workspace)" from the dropdown menu.

Alternatively, recommended extensions will appear on the "Recommended" tab, courtesy of extensions.json.

## Workspace Configuration

The `.vscode/settings.json` file includes a set of general settings and Python-specific settings for the extensions. It takes precedence over the user (general) VS Code `settings.json` file.

### General Settings

- Ensure settings specific to the workspace to avoid conflicts with global settings.
- Move general settings to the user settings file if they need to apply to all projects.

### Python-specific Settings

The workspace configuration file includes settings for the following extensions:

- `Python`
  - Includes `Pylance`, `Python Debugger`
- `Jupyter`
  - Includes `Jupyter Cell Tags`, `Jupyter Keymap`, `Jupyter Notebook Renderer`, `Jupyter Slide Show`
- `Flake8`
- `Pylint`
- `Mypy Type Checker`
- `Ruff`

These extensions help maintain code quality and streamline the development process.
