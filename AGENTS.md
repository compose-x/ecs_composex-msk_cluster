# ECS Compose-X MSK Cluster - Agent Guidelines

## Build/Lint/Test Commands
- **Format code**: `make conform` (runs isort + black)
- **Lint**: `make lint` (flake8 on ecs_composex_msk_cluster and tests)
- **Run tests**: `make test` (pytest on tests/)
- **Run single test**: `pytest -svx tests/path/to/test_file.py::test_function`
- **Coverage**: `make coverage` (behave features + coverage report)
- **Build package**: `make dist` (poetry build)

## Code Style Guidelines
- **Python**: ^3.9, use `from __future__ import annotations`
- **Formatting**: Black (line-length 88), isort with black profile
- **Imports**: Group standard library, third-party, then first-party
- **Type hints**: Use TYPE_CHECKING for imports, annotate all function signatures
- **Error handling**: Use LOG from ecs_composex.common.logging
- **Naming**: PascalCase for classes, snake_case for functions/variables
- **File headers**: Include SPDX license and copyright notice
- **JSON**: Remove BOM from all JSON files
- **Pre-commit**: Hooks enforce formatting, pyupgrade (--py38-plus), and security checks

## File Management Rules
- **NEVER delete files directly** - create `.trash` directory if it doesn't exist
- **Move unwanted files to `.trash/` with timestamp prefix**: `mv file.txt .trash/$(date +%s)_file.txt`
- **Use `stat -c %Y file.txt` for file's last-modified timestamp or `date +%s` for current time**

## Package Management
- **Use poetry for all package operations**: `poetry install`, `poetry add`, `poetry update`
- **Activate virtualenv**: `poetry shell` before running any Python commands
- **Run commands in poetry environment**: `poetry run pytest`, `poetry run black`, etc.
- **Never use pip directly** - always use poetry commands