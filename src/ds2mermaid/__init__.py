"""
Mermaid diagram subclass and helper functions.
"""

import logging
import re
from importlib.metadata import version
from shutil import which
from typing import List, Optional

from python_to_mermaid import MermaidDiagram

__version__ = version('ds2mermaid')

__all__ = [
    "MermaidGraph",
    "__version__",
    "check_for_doorstop",
    "create_subgraph_diagram",
    "get_doorstop_doc_tree",
]


class MermaidGraph(MermaidDiagram):
    """
    A mermaid subclass for generating subgraph diagrams.
    """

    def __init__(
        self,
        diagram_type: str = "graph",
        diagram_direction: str = "TB",
        subgraphs: Optional[List] = None,
    ):
        super().__init__(diagram_type)
        self.subgraphs = subgraphs
        self.set_direction(diagram_direction)

    def to_subgraph(self) -> str:
        """Convert the diagram to Mermaid syntax."""
        lines = [f"{self.diagram_type} {self.direction}"]

        # Add nodes
        for node in self.nodes:
            node_str = f"    {node.id}"
            if node.shape:
                if isinstance(node.shape, tuple):
                    start, end = node.shape
                else:
                    start, end = self.SHAPE_MAP[node.shape]
                node_str += f"{start}{node.label or ''}{end}"
            elif node.label:
                node_str += f'["{node.label}"]'

            if node.style:
                style_str = ",".join(f"{k}:{v}" for k, v in node.style.items())
                node_str += f" style {node.id} {style_str}"
            lines.append(node_str)

        # Add edges
        for edge in self.edges:
            edge_str = f"    {edge.source} {edge.style} {edge.target}"
            if edge.label:
                edge_str += f"|{edge.label}|"
            lines.append(edge_str)

        return "\n".join(lines)


def check_for_doorstop() -> str:
    """
    Make sure we can find the ``doorstop`` binary in the user environment
    and return a path string.

    :returns: program path string
    """
    doorstop_path: Optional[str] = None
    doorstop_path = which('doorstop')
    if not doorstop_path:
        logging.warning('Cannot continue, no path found for doorstop')
        raise FileNotFoundError("doorstop not found in PATH")
    return doorstop_path


def create_subgraph_diagram(prefixes: Optional[List] = None) -> MermaidGraph:
    """
    Create a new graph diagram with subgraphs.
    """
    return MermaidGraph(subgraphs=prefixes)


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
