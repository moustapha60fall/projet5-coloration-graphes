# greedy.py

def greedy_coloring(adj, order=None):
    """Simple greedy graph coloring."""
    n = len(adj)
    if order is None:
        order = list(range(n))

    colors = [0] * n

    for v in order:
        forbidden = set(colors[u] for u in adj[v] if colors[u] != 0)
        c = 1
        while c in forbidden:
            c += 1
        colors[v] = c

    return colors
