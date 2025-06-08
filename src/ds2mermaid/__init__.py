"""
Example just for package template. Replace with your own code.
"""

import re
from importlib.metadata import version
from typing import List

__version__ = version('ds2mermaid')

__all__ = [
    "__version__",
    "get_doorstop_doc_tree",
]


def get_doorstop_doc_tree(tree: str) -> List[str]:
    """
    Parse the doorstop tree structure to get a list of document prefixes,
    starting with the root doc. The string repr looks like a simple ascii
    diagram::

        tree            <Tree TUI <- [ TST, SDD ]>
        str(tree)       TUI <- [ TST, SDD ]

    :param tree: doorstop tree cast to a str
    :returns: list of document prefixes
    """
    slist: List = []
    string = str(tree)
    idp = re.compile(r'[\[\-<>, \]]')
    slist = [x for x in idp.split(string) if x != '']
    return slist
