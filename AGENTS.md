# Agent Guidelines for n8nHelper

This document provides guidelines for agentic coding agents working on the n8nHelper project.

## Project Overview

- **Project Name**: n8nHelper
- **Type**: Python Desktop Application (Streamlit UI + Socket Server)
- **Python Version**: >=3.12
- **Architecture**: Two-file split (app.py + main.py)
- **Dependencies**: asyncio, numpy, requests, streamlit, streamlit-desktop-app, watcher-cli

## Build, Lint, and Test Commands

### Installation

```bash
# Using uv (recommended for this project)
uv sync

# Or using pip
pip install -e .
```

### Running the Application

```bash
# Development - run Streamlit in browser (for testing UI)
uv run streamlit run app.py

# Production - run as desktop app (no browser required)
uv run python main.py
```

### Testing

The project currently has no test infrastructure. Tests should be added using **pytest**.

```bash
# Run all tests
pytest

# Run a single test file
pytest tests/

# Run a single test function (Recommended)
pytest tests/test_file.py::test_function_name

# Run tests matching a pattern
pytest -k "test_pattern"

# Run with verbose output
pytest -v

# Run with coverage (if coverage is installed)
pytest --cov=. --cov-report=term-missing
```

### Linting and Formatting

The following tools are recommended for this project:

```bash
# Install development dependencies
pip install -e ".[dev]"  # if defined in pyproject.toml

# Run Ruff (fast linter)
ruff check .
ruff check --fix .  # auto-fix issues

# Run Ruff formatting
ruff format .

# Run mypy type checking
mypy .

# Run all linters (if using pre-commit)
pre-commit run --all-files
```

### Type Checking

```bash
# Full type check with mypy
mypy .

# Strict mode
mypy --strict .
```

## Code Style Guidelines

### General Principles

- **Follow PEP 8** for Python code style
- **Use type hints** for all function signatures and variables where beneficial
- **Keep functions small** and focused on a single responsibility
- **Write docstrings** for all public functions and classes

### Import Guidelines

```python
# Standard library imports first
import queue
import socket
import threading

# Third-party imports second (alphabetically within group)
import requests as rq
import streamlit as st

# Local imports last (if any)
# from . import module
```

### Naming Conventions

```python
# Variables: snake_case
field_data = ""
client_message = ""

# Constants: SCREAMING_SNAKE_CASE
MAX_CONNECTIONS = 10
DEFAULT_TIMEOUT = 30

# Functions: snake_case
def send_auto():
def process_request():

# Classes: PascalCase
class DataProcessor:
class SocketServer:

# Private methods: _prefix
def _internal_method(self):
```

### Type Annotations

```python
# Always use type hints for function parameters and return types
def send_auto(url: str = "http://localhost:5678") -> dict:
    """Send data to webhook endpoint.
    
    Args:
        url: The webhook URL to send data to.
        
    Returns:
        Response data as dictionary.
    """
    payload: dict[str, str] = {"prompt": field_data}
    return rq.post(url=url, data=payload).json()

# Use | instead of Optional for Python 3.10+
def process(value: str | None) -> int:
    return len(value) if value else 0
```

### Formatting

- **Line length**: Maximum 100 characters (soft limit at 120)
- **Indentation**: 4 spaces (no tabs)
- **Blank lines**: Two blank lines between top-level definitions
- **Trailing whitespace**: Remove all trailing whitespace
- Use **Ruff formatter** for automatic formatting:

```bash
ruff format .
```

### Error Handling

```python
# Always use specific exception types
try:
    result = client.recv(1024).decode()
except UnicodeDecodeError as e:
    logger.error(f"Failed to decode message: {e}")
    result = b""

# Use context managers for resources
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(("0.0.0.0", 2008))
    server.listen(2)
    # Socket automatically closed

# Never bare except clauses
# BAD: except:
# GOOD: except Exception as e:
```

### Logging

- Use the `logging` module for application logging
- Use appropriate log levels:
  - `DEBUG`: Detailed diagnostic information
  - `INFO`: Confirmation things work as expected
  - `WARNING`: Something unexpected happened, but software still works
  - `ERROR`: Serious problem, software has failed to perform function
  - `CRITICAL`: Very serious error, program may crash

```python
import logging

logger = logging.getLogger(__name__)

def process_request():
    logger.info("Processing request received")
    # ... processing logic
```

### Async/Await

- Use `asyncio` for concurrent operations
- Avoid blocking calls in async functions
- Use `run_in_executor` for CPU-bound operations

### GUI Development (Streamlit)

- Use Streamlit for all UI components
- Keep UI in `app.py`, business logic in separate modules
- Use `st.session_state` for persistent state across reruns
- Use `st.text_area`, `st.button`, `st.input` for form elements
- Use `st.container()` and `st.columns()` for layout
- Run Streamlit in headless mode when embedding in desktop app

### Desktop App Wrapper (streamlit-desktop-app)

- Use `start_desktop_app()` from `streamlit_desktop_app` in `main.py`
- This wraps Streamlit in a native desktop window (pywebview)
- No browser required for end users
- The desktop wrapper handles its own internal threading

### Threading

- Use `threading.Thread` with `daemon=True` for background services
- Always use thread-safe data structures (`queue.Queue`, `queue.LifoQueue`)
- Avoid shared state between threads when possible
- **Architecture note**: The desktop app wrapper (`start_desktop_app`) manages its own internal threading for the web server and window. Only the socket server needs a manual daemon thread.

## File Organization

```
n8nHelper/
├── main.py              # Application entry point (starts socket server + desktop wrapper)
├── app.py               # Streamlit UI components
├── pyproject.toml       # Project configuration
├── README.md            # Project documentation
├── AGENTS.md            # This file (for agents)
└── tests/               # Test directory (create if needed)
    ├── __init__.py
    └── test_main.py
```

## Pre-commit Hooks (Recommended)

Install pre-commit for automatic code quality checks:

```bash
pip install pre-commit
pre-commit install

# Create .pre-commit-config.yaml:
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.8.0
    hooks:
      - id: ruff
      - id: ruff-format
```

## Cursor/Copilot Rules

No existing Cursor rules (`.cursor/rules/`, `.cursorrules`) or Copilot rules (`.github/copilot-instructions.md`) found in this repository.

## Key Notes for Agents

1. **Always test your changes** before marking a task as complete
2. **Run linting** (`ruff check .`) before committing
3. **Use type hints** - this project targets Python 3.12+
4. **Keep imports organized** - stdlib, third-party, local
5. **Handle exceptions properly** - never use bare `except:` clauses
6. **Write descriptive commit messages** explaining the "why", not just the "what"
