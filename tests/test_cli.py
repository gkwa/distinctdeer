from pathlib import Path

import pytest

from distinctdeer import parser_config


@pytest.fixture
def test_markdown_path():
    return Path(__file__).parent / "test_markdown.md"


def test_get_args_default(monkeypatch):
    monkeypatch.setattr("sys.argv", ["script"])
    args = parser_config.get_args()
    assert args.command is None
    assert isinstance(args.path, Path)


def test_get_args_with_command(monkeypatch):
    monkeypatch.setattr("sys.argv", ["script", "get", "used"])
    args = parser_config.get_args()
    assert args.command == "get"
    assert args.subcommand == "used"


def test_get_args_with_path(monkeypatch, test_markdown_path):
    monkeypatch.setattr(
        "sys.argv", ["script", "--path", str(test_markdown_path), "get", "all"]
    )
    args = parser_config.get_args()
    assert args.command == "get"
    assert args.subcommand == "all"
    assert args.path == test_markdown_path


def test_get_args_with_use_command(monkeypatch):
    monkeypatch.setattr("sys.argv", ["script", "use", "rand"])
    args = parser_config.get_args()
    assert args.command == "use"
    assert args.subcommand == "rand"


def test_get_args_with_check_command(monkeypatch):
    monkeypatch.setattr("sys.argv", ["script", "use", "check", "test-name"])
    args = parser_config.get_args()
    assert args.command == "use"
    assert args.subcommand == "check"
    assert args.name == "test-name"


def test_get_args_with_get_rand_command(monkeypatch):
    monkeypatch.setattr("sys.argv", ["script", "get", "rand"])
    args = parser_config.get_args()
    assert args.command == "get"
    assert args.subcommand == "rand"
