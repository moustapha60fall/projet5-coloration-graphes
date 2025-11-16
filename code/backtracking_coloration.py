# backtracking_coloration.py

def is_safe(v, color, adj, colors):
    """Check if the color can be assigned to vertex v."""
    for u in adj[v]:
        if colors[u] == color:
            return False
    return True


def backtrack_color(adj, k, colors, order, idx=0):
    """Recursive backtracking solver for k-coloring."""
    n = len(order)
    if idx == n:
        return True

    v = order[idx]
    for c in range(1, k+1):
        if is_safe(v, c, adj, colors):
            colors[v] = c
            if backtrack_color(adj, k, colors, order, idx+1):
                return True
            colors[v] = 0
    return False


def exact_k_coloring(adj, k):
    """Solve exact k-coloring using backtracking."""
    n = len(adj)
    colors = [0] * n
    order = sorted(range(n), key=lambda x: len(adj[x]), reverse=True)
    ok = backtrack_color(adj, k, colors, order)

    return colors if ok else None
