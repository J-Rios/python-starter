# Quick Start Guide

Get started with the project in 5 minutes.

## Prerequisites

- Linux (Ubuntu 18.04+ or Debian 10+)
- Python 3.12 or higher
- Git
- Make (optional)

## Project Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd python-starter
```

### 2. Setup development environment

**Option A: Using Make (Recommended)**

```bash
make setup
```

**Option B: Manual**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements_dev.txt  # Optional: for development
deactivate
```

## Running the Application

### Local Development

Start the application locally:

```bash
make start
```

Or manually:

```bash
source .venv/bin/activate
python3 src/app.py --user alice --id 123
deactivate
```

View logs:

```bash
make log
```

Stop the application:

```bash
make stop
```

### Check Status

```bash
make status
```

## Development Workflow

### Running Tests

```bash
make test
```

### Code Quality Checks

```bash
# Check code style
make lint

# Format code
make format
```

### Clean Up

```bash
make clean
```

## Configuration

Edit `config.sh` to customize:
- `APP_NAME` - Application name
- `APP_ENTRY` - Entry point script (app.py)
- `APP_DIR` - Installation directory (/opt/streamlit-starter)
- `LOG_DIR` - Log directory (/var/log/streamlit-starter)

## System Installation (Linux)

Install as a system service that runs automatically:

```bash
sudo make install
```

This will:
- Install to `/opt/streamlit-starter`
- Setup logs at `/var/log/streamlit-starter`
- Enable auto-start on boot

### Manage the Service

```bash
# View status
systemctl status streamlit-starter

# View logs
journalctl -u streamlit-starter -f

# Restart
sudo systemctl restart streamlit-starter

# Stop
sudo systemctl stop streamlit-starter
```

### Uninstall

```bash
sudo make uninstall
```

## Troubleshooting

### "make setup" fails

```bash
# Ensure Python 3.12+ is installed
python3 --version

# Try manually
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Application won't start

```bash
# Check logs
make log

# Verify virtual environment
source .venv/bin/activate
python3 -c "import sys; print(sys.executable)"
```

### Installation fails

```bash
# Check permissions
sudo ls -la /opt/streamlit-starter

# Check service
sudo systemctl status streamlit-starter

# View detailed logs
sudo journalctl -u streamlit-starter -n 100
```

## Next Steps

1. **Read the full README**: `cat README.md`
2. **Check project structure**: `tree -L 2` or `ls -la`
3. **Modify configuration**: Edit `config.sh`
4. **Customize your app**: Edit `src/app.py`
5. **Add dependencies**: Edit `requirements.txt`, then run `make setup`

## Getting Help

- Check `README.md` for detailed documentation
- See `DEPLOYMENT.md` for installation details
- Review `CONTRIBUTING.md` for development guidelines
- Run `make help` to see all available commands

## Key Commands

```bash
make help       # Show all available commands
make setup      # Initialize development environment
make start      # Run application locally
make test       # Run unit tests
make lint       # Check code quality
make format     # Auto-format code
sudo make install      # Install as system service
sudo make uninstall    # Remove system service
```
