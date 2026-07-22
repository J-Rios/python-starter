#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Test module for project_info.py.

Tests for PROJECT metadata.
"""

###############################################################################
# Libraries
###############################################################################

import pytest

from project_info import PROJECT

###############################################################################
# Tests
###############################################################################


class TestProjectInfo:
    """Test cases for PROJECT metadata."""

    def test_project_name(self):
        """Test that project name is defined."""
        assert PROJECT.NAME == "Python Starter"
        assert isinstance(PROJECT.NAME, str)

    def test_project_version(self):
        """Test that project version is defined and valid."""
        assert PROJECT.VERSION == "1.0.0"
        assert isinstance(PROJECT.VERSION, str)

    def test_project_author(self):
        """Test that project author is defined."""
        assert PROJECT.AUTHOR == "sonnen GmbH"
        assert isinstance(PROJECT.AUTHOR, str)

    def test_project_info_1(self):
        """Test that PROJECT.INFO_1 is properly formatted."""
        assert "Python Starter" in PROJECT.INFO_1
        assert "1.0.0" in PROJECT.INFO_1
        assert "(" in PROJECT.INFO_1
        assert ")" in PROJECT.INFO_1


###############################################################################
# Runnable Script Detection
###############################################################################

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
