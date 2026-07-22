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

# B) Or install it as a Linux service
make install

# B) Uninstall it
make uninstall
```

## Extra Documents

- **[QUICKSTART.md](doc/readme/QUICKSTART.md)** - Get started in 5 minutes
- **[DEPLOYMENT.md](doc/readme/DEPLOYMENT.md)** - System installation & management

## Features

- 🏗️ Well-organized project structure
- 🔧 One-command setup with `make setup`
- 💻 Local development mode (`make start`)
- 🐧 Linux systemd service integration (`sudo make install`)
- 📝 Comprehensive logging
- 🧪 Unit testing with pytest
- 🎨 Code formatting (black, isort)
- 🔍 Linting (flake8, pylint, pyright)
- 📦 Type checking (mypy)
- 🚀 Production-ready configuration
- 🔄 Centralized configuration system

## Configuration

All configuration is centralized in `config.sh`:

```bash
APP_NAME="python-starter"         # Application name
APP_ENTRY="app.py"                # Entry point script
APP_DIR="/opt/python-starter"     # Installation directory
LOG_DIR="/var/log/python-starter" # Log directory
```

Edit `config.sh` to customize the application (i.e. for installation).

## Linux Installation

Install as a system service that auto-starts on boot:

```bash
make install
```

This will:
- Create a system user `python-starter`
- Install to `/opt/python-starter`
- Setup logging at `/var/log/python-starter`
- Enable auto-start via systemd

Manage the service:
```bash
systemctl status python-starter
sudo systemctl restart python-starter
journalctl -u python-starter -f
```

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

**App won't start:**
```bash
make log           # Check logs
make errors        # Check for errors
```

**System installation issues:**
```bash
sudo systemctl status python-starter
sudo journalctl -u python-starter -n 100
```

## Useful Links

- [Python Packaging Guide](https://packaging.python.org/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [pytest Documentation](https://docs.pytest.org/)
- [systemd Documentation](https://wiki.debian.org/systemd)
