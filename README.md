[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

# Sample Python Project

A skeleton Python project with best practices for development, code quality, and tooling.

## Introduction

This project provides a structured and opinionated setup, including:

- Virtual Environment management
- Linting, formatting, static type checking
- Testing and coverage
- VS Code integration
- Pre-commit hooks

Follow the documentation to configure your environment and tools.

This is an example Python repository that can be adapted to any project. To adapt your project, you can follow the [project migration notes](./docs/MIGRATION.md).

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Setting up a Virtual Environment](#setting-up-a-virtual-environment)
- [Running the application](#running-the-application)
- [Development](#development)
- [Code Quality](#code-quality)
- [Visual Studio Code](#visual-studio-code)
- [License](#license)
- [Contact](#contact)
- [Appendix](#appendix)

## Prerequisites

- Linux OS or WSL2 on Windows
- VS Code
- Python 3.7+

## Setting up a Virtual Environment

Virtual environments isolate project dependencies. Use `venv` or the experimental Rust-based `uv`. See the Appendix for more info on [uv](#installing-uv).

### Create and activate a Virtual Environment

```bash
python3 -m venv .venv  # using venv
# or
uv venv  # using uv (if installed)
source .venv/bin/activate
```

### Install Required Packages

Use `pyproject.toml` for modern dependency management.

```bash
pip install -r pyproject.toml
# or
uv pip install -r pyproject.toml  # using uv
```

Lock dependencies:

```bash
pip freeze > requirements.txt
```

## Running the application

Activate the virtual environment and run:

```bash
export PYTHONPATH="$PWD:$PYTHONPATH"
python3 -m src.main  # Adjust 'src.main' to your module's entry point
```

## Development

Install development dependencies:

```bash
pip install -r requirements-dev.txt
# or
uv pip install -r requirements-dev.txt  # using uv
```

## Code Quality

Maintain code quality with the following tools.

### Linting

Code standards are upheld by using the following packages: `ruff`, `flake8`, `pylint`, and `mypy`. The first three are linters, and perform similar, overlapping, linting functions, while `mypy` focuses on static type checking. Their configurations are predefined but can be tailored to meet the application's specific requirements.

```bash
ruff check [file]  # to list issues
ruff check --fix [file]  # to auto-fix issues
flake8 **/*.py
pylint **/*.py
mypy **/*.py
```

### Formatting

Use ruff for consistent code style.

```bash
ruff format [file]  # to format all files, or a single one
ruff format --diff [file]  # to print the proposed changes
```

### Testing and Coverage

Run tests and check coverage with `pytest` and `coverage`.

```bash
pytest  # to run the whole suite of tests
coverage run -m pytest  # to generate a coverage report
coverage report -m  # to see the report
```

### pre-commit checks

Automate checks with pre-commit. `pre-commit` integrates with git, running specified hooks before certain git commands. This setup ensures that tests, linting, and formatting are automatically performed, promoting consistent code quality.

```sh
pre-commit install
pre-commit run --all-files
pre-commit autoupdate
```

To bypass a hook temporarily, for instance, to address a failed test in a subsequent commit:

```sh
SKIP pytest-check git commit -m "Commit message.."
```

To run the hooks outside of git commands, use `pre-commit run`. To update the hooks, use `pre-commit autoupdate`, and then commit the changes.

## Visual Studio Code

Specific information about using VS Code for development are given [here](./docs/VSCODE.md).

## License

The project is operating under an [MIT](./LICENSE) license.

## Contact

For questions or suggestions, please contact us at [email](mailto:m.alexandrakis@qmul.ac.uk) or open an issue.

## Appendix

### Installing `uv`

Install `uv` via [official documentation](https://github.com/astral-sh/uv?tab=readme-ov-file#getting-started). Update `uv` with:

```bash
uv self update
```

### Using `uv`

```bash
uv venv
source .venv/bin/activate
uv pip install -r pyproject.toml
uv pip install -r requirements-dev.txt
```
