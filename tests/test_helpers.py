import logging
from pathlib import Path

import pytest
from munch import Munch

from ds2mermaid import (
    __version__,
    check_for_doorstop,
    get_doorstop_doc_tree,
)


def test_get_doorstop_doc_tree():
    tree_string = 'TUI <- [ TST, SDD ]'
    expected = ['TUI', 'TST', 'SDD']
    prefix_list = get_doorstop_doc_tree(tree_string)
    assert prefix_list == expected
    print(prefix_list)


def test_check_for_doorstop():
    doorstop = check_for_doorstop()
    assert 'doorstop' in doorstop


def test_check_for_doorstop_bogus(monkeypatch, caplog):
    monkeypatch.setenv("PATH", "/usr/local/bin")
    caplog.set_level(logging.WARNING)
    with pytest.raises(FileNotFoundError) as excinfo:
        doorstop = check_for_doorstop()
    print(str(excinfo.value))
    assert "doorstop not found" in str(excinfo.value)
    # print(caplog.text)
    assert "Cannot continue" in caplog.text
