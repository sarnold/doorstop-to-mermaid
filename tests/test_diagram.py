import pytest

from ds2mermaid import MermaidGraph, create_subgraph_diagram


def test_graph_diagram():
    """
    Test if MermaidGraph has the right attributes and default diagram type.
    Partially verifies REQ003
    """
    graph = MermaidGraph(diagram_direction="TD")
    assert isinstance(graph, MermaidGraph)
    assert graph.diagram_type == "graph"
    assert graph.direction == "TD"


def test_create_subgraph_attrs():
    graph = create_subgraph_diagram()
    assert isinstance(graph, MermaidGraph)
    assert hasattr(graph, 'add_node')
    assert hasattr(graph, 'add_edge')
    assert graph.diagram_type == "graph"
    assert graph.direction == "TB"


def test_create_subgraph_empty():
    """
    Create an empty diagram with default type and direction.
    Verifies REQ004
    Partially verifies REQ002
    """
    graph = create_subgraph_diagram()
    expected = "graph TB"
    assert isinstance(graph, MermaidGraph)
    assert graph.to_mermaid() == expected
    print(str(graph))
    print(expected)
