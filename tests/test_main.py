"""Tests for the entry point."""

from hacs_action.__main__ import main


def test_main_succeeds() -> None:
    """The placeholder entry point exits successfully."""
    assert main() == 0
