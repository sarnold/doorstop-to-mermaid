#!/usr/bin/env python

"""
Generate mermaid diagram source from a doorstop document tree.
"""

import argparse
import sys
from typing import List

import doorstop

from ds2mermaid import __version__ as VERSION
from ds2mermaid import create_subgraph_diagram, get_doorstop_doc_tree

TREE = doorstop.core.build()


def create_diagram(debug: bool) -> str:
    """
    Collect some doorstop data and build a mermaid diagram.

    :returns: mermaid diagram text
    """
    tree: List = get_doorstop_doc_tree(str(TREE))
    if debug:
        print(f"Found prefixes: {tree}")
    graph = create_subgraph_diagram(tree)

    for doc_n, document in enumerate(TREE.documents, start=1):
        if doc_n > 4:
            continue
        for _i, item in enumerate(document.items, start=1):
            graph.add_node(item.uid.value)
            for link in item.links:
                graph.add_edge(item.uid.value, link.value, style="---->")

    return str(graph.to_subgraph())


def main(argv=None):
    """
    Gather arguments and update settings.
    """
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Example calling script for ds2mermaid',
    )
    parser.add_argument('--version', action="version", version=f"%(prog)s {VERSION}")
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        dest="verbose",
        help="display more logging info",
    )

    args = parser.parse_args()

    out = create_diagram(args.verbose)
    sys.stdout.write(out + '\n')


if __name__ == '__main__':
    raise SystemExit(main())
