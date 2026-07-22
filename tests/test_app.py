#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Test module for app.py.

Tests for app application logic.
"""

###############################################################################
# Libraries
###############################################################################

import pytest

from app import RC, parse_args

###############################################################################
# Tests
###############################################################################


class TestParseArgs:
    """Test cases for argument parsing."""

    def test_parse_args_with_user(self):
        """Test parsing with user argument."""
        args = parse_args(["--user", "alice"])
        assert args.user == "alice"

    def test_parse_args_with_id(self):
        """Test parsing with custom ID."""
        args = parse_args(["--id", "123"])
        assert args.id == 123

    def test_parse_args_default_id(self):
        """Test that default ID is 42."""
        args = parse_args([])
        assert args.id == 42

    def test_parse_args_combined(self):
        """Test parsing with multiple arguments."""
        args = parse_args(["--user", "bob", "--id", "456"])
        assert args.user == "bob"
        assert args.id == 456


class TestReturnCodes:
    """Test cases for return codes."""

    def test_rc_success(self):
        """Test SUCCESS return code."""
        assert RC.SUCCESS == 0

    def test_rc_failure(self):
        """Test FAILURE return code."""
        assert RC.FAILURE == 1

    def test_rc_invalid_args(self):
        """Test INVALID_ARGS return code."""
        assert RC.INVALID_ARGS == 2


###############################################################################
# Runnable Script Detection
###############################################################################

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
