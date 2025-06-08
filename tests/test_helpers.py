from pathlib import Path

import pytest
from munch import Munch

from ds2mermaid import get_doorstop_doc_tree, version


def test_get_doorstop_doc_tree():
    tree_string = 'TUI <- [ TST, SDD ]'
    expected = ['TUI', 'TST', 'SDD']
    prefix_list = get_doorstop_doc_tree(tree_string)
    assert prefix_list == expected
    print(prefix_list)
