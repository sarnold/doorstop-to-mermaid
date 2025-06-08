import pytest

from ds2mermaid import MermaidGraph, create_subgraph_diagram


def test_MermaidGraph():
    graph = MermaidGraph()
    assert isinstance(graph, MermaidGraph)
    assert hasattr(graph, 'add_node')
    assert hasattr(graph, 'add_edge')
    assert graph.diagram_type == "graph"
    assert graph.direction == "TB"


def test_create_subgraph_diagram():
    graph = create_subgraph_diagram()
    assert isinstance(graph, MermaidGraph)
    assert hasattr(graph, 'add_node')
    assert hasattr(graph, 'add_edge')
    assert graph.diagram_type == "graph"
    assert graph.direction == "TB"


def test_empty_subgraph_diagram():
    graph = create_subgraph_diagram()
    expected = "graph TB"
    assert isinstance(graph, MermaidGraph)
    assert graph.to_mermaid() == expected
    print(str(graph))
    print(expected)
