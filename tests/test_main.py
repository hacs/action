"""Tests for the entry point."""

from hacs_action.__main__ import main


def test_main_succeeds() -> None:
    assert main() == 0
