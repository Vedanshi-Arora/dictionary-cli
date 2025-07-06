import pytest
from click.testing import CliRunner
from dictionary_cli.main import cli

def test_dictionary_cli_basic():
    runner = CliRunner()
    result = runner.invoke(cli, ['test'])
    assert result.exit_code == 0

def test_dictionary_cli_empty_word():
    runner = CliRunner()
    result = runner.invoke(cli, [])
    assert result.exit_code != 0

