from click.testing import CliRunner
from eslog.release import __version__
from eslog.main import cli


runner = CliRunner()


def test_version():
    assert __version__ == "0.0.3"


def test_list_help():
    result = runner.invoke(cli, ["list", "--help"])
    assert result.exit_code == 0
    assert "List all indexes" in result.output


def test_logs_help():
    result = runner.invoke(cli, ["logs", "--help"])
    assert result.exit_code == 0
    assert " Get and archive logs" in result.output
