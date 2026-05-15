"""Smoke tests for the loader CLI.

These tests do not hit AWS or any database. They confirm the Typer app is
wired up and every documented subcommand is registered.
"""

from __future__ import annotations

from typer.testing import CliRunner

from loader.people_api.cli import app

runner = CliRunner()

EXPECTED_COMMANDS = {
    "inspect-prod",
    "unload",
    "provision",
    "create-schema",
    "copy",
    "build-indexes",
    "resize",
    "validate",
    "teardown",
    "status",
}


def test_help_lists_all_subcommands() -> None:
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0, result.output
    for cmd in EXPECTED_COMMANDS:
        assert cmd in result.output, f"missing subcommand {cmd!r} in --help output"


def test_status_help_renders() -> None:
    result = runner.invoke(app, ["status", "--help"])
    assert result.exit_code == 0, result.output
    assert "--date" in result.output
