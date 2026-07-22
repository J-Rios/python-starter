#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Python Tool main script.

This module contains the main application logic.
"""

###############################################################################
# Standard Libraries
###############################################################################

# Argparse Library
import argparse

# JSON Library
import json

# Logging Library
import logging
import logging.config

# System Library
import sys

# Time Library
import time

# Local Logging Configuration
from cfg.logging_cfg import LOGGING_CFG

# Local Project Information
from cfg.project_info import PROJECT

# Traceback Library
from traceback import format_exc


###############################################################################
# Third-Party Libraries
###############################################################################

# None


###############################################################################
# Local Libraries
###############################################################################

# User Interface Library
from ui import UserInterface


###############################################################################
# Logger Setup
###############################################################################

logging.config.dictConfig(json.loads(LOGGING_CFG))
logger = logging.getLogger(__name__)


###############################################################################
# Constants & Configurations
###############################################################################

# None


###############################################################################
# Auxiliary Data Structures
###############################################################################

class RC:
    """
    Return codes for tool process exit status code.

    Notes:
    - Linux exit codes are limited to 0-255.
    - Values above 120 are reserved so avoid them.
    """

    SUCCESS = 0
    FAILURE = 1
    INVALID_ARGS = 2
    RUNNING = 100


###############################################################################
# Global Elements
###############################################################################

# User Interface
ui = UserInterface()


###############################################################################
# Left Sidebar Panel Button Functions
###############################################################################

def sidebar_btn_0_press():
    '''UI Left Sidebar Panel Button_0 Press Handler.'''
    logger.info("Pressed Sidebar Button 0")


def sidebar_btn_1_press():
    '''UI Left Sidebar Panel Button_1 Press Handler.'''
    logger.info("Pressed Sidebar Button 1")


def sidebar_btn_2_press():
    '''UI Left Sidebar Panel Button_2 Press Handler.'''
    logger.info("Pressed Sidebar Button 2")


def sidebar_btn_3_press():
    '''UI Left Sidebar Panel Button_3 Press Handler.'''
    logger.info("Pressed Sidebar Button 3")


def btn_clickme_press():
    '''UI Click-Me Button Pressed.'''
    logger.info("Button Click-Me Pressed")


###############################################################################
# Auxiliary Functions - Main Setup & Loop
###############################################################################

def main_loop(args) -> int:
    """Application Main loop."""
    return RC.SUCCESS


def main_setup(args) -> int:
    """Application Main setup."""
    # Create UI and bind function callbacks
    ui.callbacks.sidebar_btn_0.app = sidebar_btn_0_press
    ui.callbacks.sidebar_btn_1.app = sidebar_btn_1_press
    ui.callbacks.sidebar_btn_2.app = sidebar_btn_2_press
    ui.callbacks.sidebar_btn_3.app = sidebar_btn_3_press
    ui.callbacks.btn_clickme.app = btn_clickme_press
    # Generate and show UI
    ui.setup_page(PROJECT.NAME, "centered", PROJECT.DESCRIPTION,
                  PROJECT.INFO_2)
    return RC.SUCCESS


###############################################################################
# Auxiliary Functions - CLI Argument Parsing
###############################################################################

def parse_args(argv):
    """Parse CLI arguments for remote SSH CAN connection."""
    # Parser Setup
    parser = argparse.ArgumentParser(description=f"{PROJECT.DESCRIPTION}")
    parser.add_argument(
        "--version",
        action="version",
        version=f"{PROJECT.INFO_1}",
    )
    # Mandatory Arguments
    parser.add_argument("--user", help="Input username")
    # ...
    # Optional Arguments
    parser.add_argument(
        "--id", type=int, default=42, help="Input ID (default: 42)"
    )
    # ...
    return parser.parse_args(argv)


###############################################################################
# Main Function
###############################################################################

def main(argv=None) -> int:
    """Run the main application logic."""
    rc = RC.SUCCESS
    logger.info("Starting Application...")
    args = parse_args(argv)
    rc = main_setup(args)
    if rc == RC.SUCCESS:
        while True:
            try:
                rc = main_loop(args)
                if rc != RC.RUNNING:
                    break
            except Exception as e:
                logger.error(f"Error: {e}")
                logger.error(f"{format_exc()}")
                rc = RC.FAILURE
            except KeyboardInterrupt:
                break
    logger.info("Exiting Application...")
    if rc == RC.RUNNING:
        rc = RC.FAILURE
    return rc


###############################################################################
# Runnable Script Detection
###############################################################################

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
