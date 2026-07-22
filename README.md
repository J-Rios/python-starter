# python-starter

A production-ready Python project template to be used as reference for starting new projects with it.

There are two app scripts to be used as reference for your project:

- **app.py:** Standard python script
- **app_asyncio.py:** Asynchronous python script approach using asyncio

## Quick Start

```bash
# See all available commands
make

# Setup project for development and local execution
make setup

# A) Run the application locally
make run

# A) Stop local execution
make stop
```

- **[QUICKSTART.md](doc/readme/QUICKSTART.md)** - Get started in 5 minutes

## Features

- 🏗️ Well-organized project structure
- 🔧 One-command setup (`make setup`)
- 💻 Local development mode (`make start`)
- 📝 Comprehensive logging
- 🧪 Unit testing with pytest
- 🎨 Code formatting (black, isort)
- 🔍 Linting (flake8, pylint, pyright)
- 📦 Type checking (mypy)
- 🪝 Pre-commit hooks
- 🚀 Production-ready configuration
- 🔄 Centralized configuration system

## Configuration

All configuration is centralized in `config.sh`:

```bash
APP_NAME="python-starter"         # Application name
APP_ENTRY="app.py"                # Entry point script
LOG_DIR="/var/log/python-starter" # Log directory
```

Edit `config.sh` to customize the application.


## Running Tests

```bash
make test                    # Run all tests
make test -- -v            # Run with verbose output
make test -- tests/test_app.py  # Run specific test file
```

## Local Development

```bash
# Setup (one time)
make setup

# Activate virtual environment
source .venv/bin/activate

# Install dev dependencies (optional)
pip install -r requirements_dev.txt

# Run the app
make start

# Check code quality
make lint
make format
```

## Troubleshooting

**Setup fails:**
```bash
python3 --version  # Ensure Python 3.8+
make setup         # Try again
```

**App won't start:**
```bash
make log           # Check logs
make errors        # Check for errors
```

## Useful Links

- [Python Packaging Guide](https://packaging.python.org/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [pytest Documentation](https://docs.pytest.org/)
