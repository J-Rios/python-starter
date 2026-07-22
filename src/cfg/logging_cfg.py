#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Logging configuration module.

Provides centralized logging setup for the application.
"""

###############################################################################
# Logging Setup
###############################################################################

LOGGING_CFG = """
{
    "version": 1,
    "disable_existing_loggers": false,
    "formatters": {
        "none": {
            "format": "%(message)s"
        },
        "simple": {
            "format": "[%(levelname)s] %(message)s"
        },
        "timestamped": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        "stderr": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "simple",
            "stream": "ext://sys.stderr"
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "timestamped",
            "filename": "output.log",
            "mode": "a"
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "stdout",
            "stderr",
            "file"
        ]
    }
}
"""
