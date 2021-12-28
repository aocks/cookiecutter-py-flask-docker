#!/usr/bin/env python

"""Tests for `{{ cookiecutter.project_slug }}` package."""

import pytest
from click.testing import CliRunner

from {{ cookiecutter.project_slug }} import cli


@pytest.mark.skip(reason='Example of test marked as something to skip.')
def test_example_skip():
    "Example of a test which cannot succeed so marked as skip."
    assert 1 == 0


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert '{{ cookiecutter.project_slug }}.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
