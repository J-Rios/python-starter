#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Project information module.

Provides project metadata from pyproject.toml as single source of truth.
"""

###############################################################################
# Standard Libraries
###############################################################################

import sys
from datetime import datetime
from pathlib import Path

###############################################################################
# TOML Parser (compatible with Python 3.8+)
###############################################################################


def _find_project_root():
    """Find project root by searching for pyproject.toml.

    Starts from the current module's directory and searches upward
    through parent directories until pyproject.toml is found.

    Returns:
        Path: Project root directory containing pyproject.toml

    Raises:
        FileNotFoundError: If pyproject.toml is not found
    """
    # Start from this module's directory
    current = Path(__file__).resolve().parent
    # Search up to 10 levels
    for _ in range(10):
        toml_file = current / "pyproject.toml"
        if toml_file.exists():
            return current
        # Move to parent directory
        parent = current.parent
        if parent == current:
            # Reached filesystem root
            break
        current = parent
    raise FileNotFoundError(
        "Could not find pyproject.toml. "
        "Make sure you're in or above the project root directory."
    )


def _load_toml():
    """Load pyproject.toml file."""
    # Try Python 3.11+ tomllib first
    try:
        import tomllib  # noqa: F401
    except ImportError:
        try:
            import tomli as tomllib
        except ImportError:
            raise ImportError(
                "tomllib or tomli required. Install with: pip install tomli"
            )
    # Find project root and load TOML
    project_root = _find_project_root()
    toml_file = project_root / "pyproject.toml"
    with open(toml_file, "rb") as f:
        return tomllib.load(f)


###############################################################################
# Project Metadata (from pyproject.toml)
###############################################################################


class PROJECT:
    """Project metadata loaded from pyproject.toml.

    Attributes:
        NAME: Project name.
        DESCRIPTION: Project description.
        VERSION: Project version.
        DATE: Version date.
        AUTHOR: Project author.
        URL: Project URL.
        INFO: Formatted project info string.
        INFO_1: Formatted project info string with date.
        INFO_2: Formatted project info string with date and author.
    """

    try:
        _toml_data = _load_toml()
        _project = _toml_data.get("project", {})
        _urls = _project.get("urls", {})
        # Extract metadata from pyproject.toml
        NAME = _project.get("name", "Python Project").replace("-", " ").title()
        VERSION = _project.get("version", "0.0.0")
        DESCRIPTION = _project.get("description", "")
        if _project.get("authors"):
            AUTHOR = _project["authors"][0]["name"]
        else:
            AUTHOR = "Unknown"
        URL = _urls.get("Homepage", "")
        DATE = datetime.now().date()
        # Formatted strings
        INFO = f"{NAME} v{VERSION}"
        INFO_1 = f"{NAME} v{VERSION} ({DATE.strftime('%Y-%m-%d')})"
        INFO_2 = f"{INFO_1} • {AUTHOR}"
    except Exception as e:
        # Fallback values if TOML parsing fails
        print(
            f"Warning: Could not load project info from pyproject.toml: {e}",
            file=sys.stderr,
        )
        NAME = "Python Project"
        VERSION = "0.0.0"
        DESCRIPTION = "A Python project"
        AUTHOR = "Unknown"
        URL = ""
        DATE = datetime.now().date()
        INFO = f"{NAME} v{VERSION}"
        INFO_1 = f"{NAME} v{VERSION} ({DATE.strftime('%Y-%m-%d')})"
        INFO_2 = f"{INFO_1} • {AUTHOR}"
