import pytest
from python_to_mermaid import MermaidEdge, MermaidNode

from ds2mermaid import MermaidGraph, create_subgraph_diagram


def test_graph_diagram():
    """
    Test we can modify all the defaults. Partially verifies REQ003
    """
    graph = MermaidGraph(diagram_type="flowchart", diagram_direction="TD")
    graph.add_node("A", label="Circle Node")
    graph.add_node("B", shape="rounded", label="Rounded Node")
    assert isinstance(graph, MermaidGraph)
    assert graph.diagram_type == "flowchart"
    assert graph.direction == "TD"
    print(graph.to_subgraph())


def test_direct_shape_syntax():
    """Test that direct Mermaid syntax for shapes works."""
    diagram = MermaidGraph()
    node1 = MermaidNode(
        id="A",
        label="Custom Shape",
        shape=("{{", "}}"),
        style={"fill": "#f9f", "stroke": "#333"},
    )
    diagram.add_node(node1)
    node2 = MermaidNode(id="B", label="Another Shape")
    assert "A{{Custom Shape}}" in diagram.to_subgraph()


def test_create_subgraph_attrs():
    """
    Test if MermaidGraph has the right attributes and default diagram type.
    Partially verifies REQ002
    """
    graph = create_subgraph_diagram()
    assert isinstance(graph, MermaidGraph)
    assert hasattr(graph, 'subgraphs')
    assert hasattr(graph, 'add_node')
    assert hasattr(graph, 'add_edge')
    assert graph.diagram_type == "graph"
    assert graph.direction == "TB"


def test_create_edge():
    """
    Test adding MermaidEdge with various configurations and default graph
    settings.  Verifies REQ004
    """
    # Basic edge
    edge = MermaidEdge("A", "B")
    assert edge.source == "A"
    assert edge.target == "B"
    assert edge.label is None
    assert edge.style == "-->"

    # Edge with label
    edge1 = MermaidEdge("A", "B", label="process")
    assert edge1.label == "process"

    # Edge with custom style
    edge2 = MermaidEdge("A", "B", style="===")
    assert edge2.style == "==="

    diagram = MermaidGraph()
    diagram.add_edge(edge)
    diagram.add_edge(edge1)
    diagram.add_edge(edge2)
    assert diagram.diagram_type == "graph"
    assert diagram.direction == "TB"
    assert len(diagram.edges) == 3
    assert diagram.edges[0] == edge
    print(diagram.to_subgraph())
