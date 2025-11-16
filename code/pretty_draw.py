# pretty_draw.py
import networkx as nx
import matplotlib.pyplot as plt

PALETTE = [
    "#e74c3c", "#2ecc71", "#3498db", "#9b59b6",
    "#f1c40f", "#1abc9c", "#e67e22", "#34495e",
    "#d35400", "#7f8c8d"
]


def choose_layout(adj):
    """Auto-select best layout depending on graph properties."""
    G = nx.Graph()

    for v in range(len(adj)):
        for u in adj[v]:
            if u > v:
                G.add_edge(v, u)

    degrees = [len(adj[v]) for v in range(len(adj))]

    # Cycle detection (all degrees = 2)
    if all(d == 2 for d in degrees):
        return nx.circular_layout(G)

    # Bipartite detection
    try:
        X, Y = nx.algorithms.bipartite.sets(G)
        return nx.bipartite_layout(G, X)
    except Exception:
        pass

    # Complete graph
    if max(degrees) == len(adj) - 1:
        return nx.shell_layout(G)

    return nx.spring_layout(G, seed=42)


def visualize_pretty(adj, colors, title="Pretty Coloring"):
    G = nx.Graph()

    for v in range(len(adj)):
        for u in adj[v]:
            if u > v:
                G.add_edge(v, u)

    layout = choose_layout(adj)
    color_map = [PALETTE[(c-1) % len(PALETTE)] for c in colors]

    plt.figure(figsize=(6, 6))
    nx.draw(
        G, layout,
        with_labels=True,
        node_color=color_map,
        node_size=900,
        font_size=11,
        edge_color="#555",
        width=2
    )
    plt.title(title)
    plt.show()
