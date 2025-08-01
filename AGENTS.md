## AGENTS.md

This file provides guidelines for agentic coding agents operating in this repository.

### Build and Test

- **Dependencies**: Project dependencies are managed with `uv`. Use `uv pip install -r requirements.txt` if a `requirements.txt` file is present, otherwise install from `pyproject.toml`.
- **Testing**: This project uses `pytest`. Run tests with `pytest`. To run a single test file, use `pytest path/to/test_file.py`.
- **Linting**: This project uses `ruff`. Run the linter with `ruff check .`.

### Code Style

- **Imports**: Use `isort` conventions for import ordering (standard library, third-party, then local application).
- **Formatting**: Code is formatted with `black`.
- **Types**: Use type hints for all function signatures.
- **Naming**:
    - `snake_case` for functions, methods, and variables.
    - `PascalCase` for classes.
- **Error Handling**: Use `try...except` blocks for operations that can fail, and raise specific exceptions.
- **Docstrings**: Use Google-style docstrings for all public modules, classes, and functions.
- **General**: Adhere to PEP 8 guidelines.
