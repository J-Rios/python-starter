#!/usr/bin/env bash

###############################################################################
# Project Configuration - Centralized Settings
###############################################################################
# This file contains all configuration for the project.
# Modify this file to customize the application behavior.

# Application name (used for service, user, directories)
export APP_NAME="python-starter"

# Application entry point (relative to src/)
export APP_ENTRY="app.py"

# Service user and group (for system installation)
# Set to "root" to run as root, or any other user for dedicated user
export APP_USER="root"
export APP_GROUP="root"

# Installation directories (system-wide)
export APP_DIR="/opt/${APP_NAME}"
export LOG_DIR="/var/log/${APP_NAME}"

# Development directories (local)
export VENV_DIR=".venv"
export DEV_LOG_FILE="output.log"

# Python configuration
export PYTHON_CMD="python3"
export PIP_CMD="${VENV_DIR}/bin/pip"

# Get project root directory
export PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

###############################################################################
# Utility Functions
###############################################################################

log_info() {
    echo "[INFO] $1"
}

log_error() {
    echo "[ERROR] $1" >&2
}

log_warn() {
    echo "[WARN] $1"
}

log_success() {
    echo "[SUCCESS] $1"
}

check_root() {
    if [ "$(id -u)" != "0" ]; then
        log_error "This operation requires root privileges (sudo)"
        return 1
    fi
    return 0
}

check_venv() {
    if [ ! -d "${VENV_DIR}" ]; then
        log_error "Virtual environment not found at ${VENV_DIR}"
        log_info "Run 'make setup' to create it"
        return 1
    fi
    return 0
}

source_venv() {
    if ! check_venv; then
        return 1
    fi
    source "${VENV_DIR}/bin/activate"
    return 0
}

###############################################################################
