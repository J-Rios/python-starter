#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Python Tool main script with asyncio support.

This module contains the main application logic using asyncio
for asynchronous execution.
"""

###############################################################################
# Standard Libraries
###############################################################################

# Argparse Library
import argparse

# Asyncio Library
import asyncio

# JSON Library
import json

# Logging Library
import logging
import logging.config

# System Library
import sys

# Traceback Library
from traceback import format_exc

# Local Logging Configuration
from cfg.logging_cfg import LOGGING_CFG

# Local Project Information
from cfg.project_info import PROJECT


###############################################################################
# Third-Party Libraries
###############################################################################

# None


###############################################################################
# Local Libraries
###############################################################################


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

# None


###############################################################################
# Auxiliary Functions - Main Setup & Loop
###############################################################################

async def main_loop(args) -> int:
    """Application Main loop."""
    global uptime
    logger.info(f"Uptime: {uptime} seconds")
    uptime = uptime + 1
    if uptime == 5:
        logger.warning("a warning here")
    if uptime == 10:
        logger.error("an error here")
    await asyncio.sleep(1)
    return RC.RUNNING


async def main_setup(args) -> int:
    """Application Main setup."""
    global uptime
    uptime = 0
    logger.info("")
    logger.info(f"Hello {args.user}, your ID is {args.id}")
    logger.info("")
    logger.info("Press Ctrl+C to exit the tool...")
    logger.info("")
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
# Main Async Function
###############################################################################

async def async_main(argv=None) -> int:
    """Run the main application logic asynchronously."""
    rc = RC.SUCCESS
    logger.info("Starting Python Tool (asyncio)...")
    args = parse_args(argv)
    rc = await main_setup(args)
    if rc == RC.SUCCESS:
        try:
            while True:
                try:
                    rc = await main_loop(args)
                    if rc != RC.RUNNING:
                        break
                except asyncio.CancelledError:
                    break
        except KeyboardInterrupt:
            pass
    logger.info("Exiting Python Tool...")
    if rc == RC.RUNNING:
        rc = RC.FAILURE
    return rc


###############################################################################
# Main Function (Entry Point)
###############################################################################

def main(argv=None) -> int:
    """Run the asyncio application entry point."""
    try:
        return asyncio.run(async_main(argv))
    except KeyboardInterrupt:
        return RC.SUCCESS
    except Exception as e:
        logger.error(f"Error: {e}")
        logger.error(f"{format_exc()}")
        return RC.FAILURE


###############################################################################
# Runnable Script Detection
###############################################################################

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
