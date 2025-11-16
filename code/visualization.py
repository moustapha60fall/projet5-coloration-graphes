# visualization.py
import networkx as nx
import matplotlib.pyplot as plt

PALETTE = [
    "#e74c3c", "#2ecc71", "#3498db", "#9b59b6",
    "#f1c40f", "#1abc9c", "#e67e22", "#34495e",
    "#d35400", "#7f8c8d"
]


def visualize_coloring(adj, colors, title="Graph Coloring"):
    """Basic visualization of a colored graph."""
    G = nx.Graph()

    for v in range(len(adj)):
        for u in adj[v]:
            if u > v:
                G.add_edge(v, u)

    color_map = [PALETTE[(c-1) % len(PALETTE)] for c in colors]

    plt.figure(figsize=(5, 5))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color=color_map, node_size=700)
    plt.title(title)
    plt.show()
