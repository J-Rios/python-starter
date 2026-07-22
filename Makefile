
SHELL = /bin/bash
TOOLS := ./tools

.PHONY: help setup install uninstall run stop status log errors test lint format clean

help:
	@echo ""
	@echo "═══════════════════════════════════════════════════════════════"
	@echo "  Python Starter - Available Commands"
	@echo "═══════════════════════════════════════════════════════════════"
	@echo ""
	@echo "SETUP & DEVELOPMENT:"
	@echo "  make setup     - Initialize development environment"
	@echo "  make clean     - Clean cache, logs, and venv"
	@echo ""
	@echo "LOCAL TESTING:"
	@echo "  make run       - Start application locally"
	@echo "  make stop      - Stop running application"
	@echo "  make status    - Show application status"
	@echo "  make log       - View application logs"
	@echo ""
	@echo "CODE QUALITY:"
	@echo "  make test      - Run unit tests"
	@echo "  make lint      - Check code style (flake8, pylint)"
	@echo "  make format    - Format code (black, isort)"
	@echo ""
	@echo "SYSTEM INSTALLATION (requires sudo):"
	@echo "  make install   - Install as Linux service"
	@echo "  make uninstall - Remove service installation"
	@echo ""
	@echo "TROUBLESHOOTING:"
	@echo "  make errors    - Check for errors in logs"
	@echo "  make env-info  - Show environment information"
	@echo ""

# Development setup
setup:
	@chmod +x $(TOOLS)/setup
	@$(TOOLS)/setup

# Local testing and management
run:
	@chmod +x $(TOOLS)/run $(TOOLS)/status
	@$(TOOLS)/run

start: run

stop:
	@chmod +x $(TOOLS)/stop
	@$(TOOLS)/stop

status:
	@chmod +x $(TOOLS)/status
	@$(TOOLS)/status

log:
	@chmod +x $(TOOLS)/log
	@$(TOOLS)/log

errors:
	@chmod +x $(TOOLS)/check_errors
	@$(TOOLS)/check_errors

# Code quality checks
test:
	@bash -c 'source .venv/bin/activate 2>/dev/null || true; pytest -v tests/ || echo "Run make setup first"'

lint:
	@bash -c 'source .venv/bin/activate 2>/dev/null || true; flake8 src/ tests/ --max-line-length=80 || echo "Run make setup first"'

format:
	@bash -c 'source .venv/bin/activate 2>/dev/null || true; black src/ tests/ && isort src/ tests/ || echo "Run make setup first"'

# System-wide installation
install:
	@chmod +x $(TOOLS)/install
	@sudo $(TOOLS)/install

uninstall:
	@chmod +x $(TOOLS)/uninstall
	@sudo $(TOOLS)/uninstall

# Cleanup
clean:
	@echo "Cleaning up..."
	@rm -rf .venv
	@rm -rf build/ dist/ *.egg-info/
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*.log" -delete
	@echo "Cleanup complete!"

# Info
env-info:
	@echo ""
	@echo "Environment Information:"
	@echo "────────────────────────────────────────"
	@echo "Python version: $$(python3 --version)"
	@echo "Pip version: $$(python3 -m pip --version | cut -d' ' -f2)"
	@echo "Virtual env: .venv"
	@echo "Project root: $$(pwd)"
	@echo ""
