#!/usr/bin/env python

"""
Generate mermaid diagram source from a doorstop document tree.
"""

import argparse
import logging
import sys

import doorstop

from ds2mermaid import (  # pylint: disable=unused-import
    SubGraph,
    __version__,
    check_for_doorstop,
    create_subgraph_diagram,
    get_doorstop_doc_tree,
)

TREE = doorstop.core.build()
VERSION = __version__


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

    # basic logging setup must come before any other logging calls
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(stream=sys.stdout, level=log_level)
    # printout()  # logging_tree
    logging.info('Log level is set to %s', log_level)


if __name__ == '__main__':
    raise SystemExit(main())
