"""
Mermaid diagram subclass and helper functions.
"""

import re
from importlib.metadata import version
from typing import List

from python_to_mermaid import MermaidDiagram

__version__ = version('ds2mermaid')

__all__ = [
    "MermaidGraph",
    "__version__",
    "create_subgraph_diagram",
    "get_doorstop_doc_tree",
]


class MermaidGraph(MermaidDiagram):
    """
    A mermaid subclass for generating subgraph diagrams.
    """

    def __init__(self, diagram_type: str = "graph", diagram_direction: str = "TB"):
        super().__init__(diagram_type)
        self.set_direction(diagram_direction)


def create_subgraph_diagram() -> MermaidGraph:
    """
    Create a new graph diagram with subgraphs.
    """
    return MermaidGraph()


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
