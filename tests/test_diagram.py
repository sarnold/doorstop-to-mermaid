import pytest
from python_to_mermaid import MermaidEdge, MermaidNode

from ds2mermaid import MermaidGraph, SubGraph, create_subgraph_diagram


def test_graph_subgraph():
    """
    Test we can create and manipulate subgraph objects.
    Verifies REQ005 and REQ006 for subgraph.nodes
    """
    node_lst = [
        "REQS001",
        "REQS002",
        "REQS003",
        "REQS004",
        "REQS005",
        "REQS006",
        "REQS007",
    ]
    expected = [
        "REQS001",
        "REQS002",
        "REQS003",
        "REQS004",
        "REQS005",
        "REQS006",
        "REQS007",
    ]
    subgraph = SubGraph("REQS", node_lst)
    assert subgraph.name == "REQS"
    assert len(subgraph.nodes) == 7
    assert isinstance(subgraph.nodes, list)
    subgraph.add_node("REQS008")
    assert len(subgraph.nodes) == 8
    expected.append("REQS008")
    assert subgraph.nodes == expected
    print(subgraph.nodes)


def test_graph_diagram():
    """
    Test we can modify all the defaults. Partially verifies REQ003
    """
    graph = MermaidGraph(diagram_type="flowchart", diagram_direction="TD")
    graph.add_node("A", label="Default Node")
    graph.add_node("B", shape="rounded", label="Rounded Node")
    assert isinstance(graph, MermaidGraph)
    assert graph.diagram_type == "flowchart"
    assert graph.direction == "TD"
    print(graph.to_subgraph())


def test_direct_shape_syntax():
    """Test that direct Mermaid syntax for shapes works."""
    diagram = MermaidGraph()
    diagram.add_subgraph("Shape")
    node1 = MermaidNode(
        id="A",
        label="Custom Shape",
        shape=("{{", "}}"),
        style={"fill": "#f9f", "stroke": "#333"},
    )
    diagram.add_node(node1)
    node2 = MermaidNode(id="B", label="Another Shape", shape="diamond")
    diagram.add_node(node2)
    diagram_str = diagram.to_subgraph()
    print(diagram_str)
    assert "A{{Custom Shape}}" in diagram_str


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


def test_create_subgraph_subgraphs():
    """
    Test if MermaidGraph has the right list of subgraphs.
    Verifies REQ005 and REQ006 for graph.subgraphs
    """
    prefixes = ["REQS", "SDD", "TST"]
    expected = ["REQS", "SDD", "TST"]
    graph = create_subgraph_diagram(prefixes)
    assert isinstance(graph, MermaidGraph)
    assert graph.subgraphs == prefixes
    graph.add_subgraph("EXT")
    expected.append("EXT")
    assert graph.subgraphs == expected
    print(graph.subgraphs)


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
