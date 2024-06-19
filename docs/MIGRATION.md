# Adapting Your Project

Follow these guidelines to successfully migrate your Python project into the new structure.

- [Analyze Your Current Structure](#analyze-your-current-structure)
- [Integrate Codebase](#integrate-codebase)
- [Utilize Development Tools](#utilize-development-tools)
- [Documentation](#documentation)
- [Testing and Validation](#testing-and-validation)
- [Final Steps](#final-steps)
- [Example for New GitHub Project](#example-for-new-github-project)

## Analyze Your Current Structure

1. Identify and Organize Components:
    - Examine your codebase and categorize components: core functionality, utility functions, models, data analysis scripts, etc.
    - Organize these into modules for easy navigation and maintenance.
2. Review Dependencies:
    - List all external dependencies.
    - Update `pyproject.toml` (or `requirements.txt`) for runtime dependencies and `requirements-dev.txt` for development-only packages.

## Integrate Codebase

1. Migrate Source Code:
    - Move primary source code to `src/` directory.
    - Create sub-directories within `src/` for each module and include an empty `__init__.py`.
    - Adjust import statements as needed.
2. Adapt Tests:
    - Relocate tests to `tests/` directory.
    - Mirror project structure in `tests/` or use a flat hierarchy if few tests.
    - Update `pytest` configuration to reflect new paths.
3. Integrate Configuration Files:
    - Review and adapt existing configuration files (e.g., database, external services) to match the new structure.

## Utilize Development Tools

1. Code Quality Tools:
    - Use `flake8`, `mypy`, `pylint`, and `ruff` to review and adjust code for quality standards.
2. Pre-commit Hooks:
    - Ensure `pre-commit` hooks are installed and configured to run automatically.

## Documentation

1. Update README:
    - Modify `README.md` to reflect project specifics: purpose, running instructions, and contribution guidelines.
    - Remove or update template-specific sections.
2. Add Contributing Guide:
    - Create or update `CONTRIBUTING.md` with guidelines for contributing, including coding standards and pull request process.

## Testing and Validation

1. Run Tests:
    - Execute all tests to ensure they pass in the new setup.
2. Code Quality Checks:
    - Run linters and static type checkers to identify and fix issues.
3. Manual Testing:
    - Perform manual tests to ensure expected application behavior.

## Final Steps

1. Remove Existing Git History:

    - Detach from the template's version history:

    ```sh
    rm -rf .git
    ```

2. Initialize or Reuse Repository:
    - Follow version control instructions to add files to your new or existing repository.
3. Commit Changes:
    - Commit the integrated changes with a detailed message describing the migration process.
4. Continuous Learning:
    - Stay open to new tools and practices to enhance your development workflow.

## Example for New GitHub Project

For a new project on GitHub, after creating chosen-python-project-name, initialize and push your repository:

```sh
git init
git add .
git commit -m "Initial commit"
git branch -M master
git remote add origin git@github.com:Name/chosen-python-project-name.git
git push -u origin master
```
