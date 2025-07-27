## AGENTS.md

This file provides guidelines for agentic coding assistants operating in this repository.

### Build, Lint, and Test

- **Dependencies**: This project uses Python >= 3.12. Dependencies are not currently managed by a tool.
- **Running the code**: Execute scripts directly, e.g., `python pathlib_learning.py`.
- **Testing**: No test framework is set up. For now, manually verify changes. If you add tests, use the `unittest` module.
- **Linting**: No linter is configured. Please adhere to PEP 8 style.

### Code Style Guidelines

- **Formatting**: Follow PEP 8 guidelines. Use a line length of 88 characters.
- **Imports**: Place all imports at the top of the file, grouped into standard library, third-party, and local application imports.
- **Typing**: Add type hints for all function signatures.
- **Naming**: Use `snake_case` for variables and functions. Use `PascalCase` for classes.
- **Error Handling**: Use `try...except` blocks for operations that might fail, such as file I/O.
- **Docstrings**: Add a docstring to all new modules, functions, and classes, explaining their purpose.
