# welsh_powell.py

def welsh_powell(adj):
    """Welsh-Powell graph coloring algorithm."""
    n = len(adj)
    degrees = [(i, len(adj[i])) for i in range(n)]
    degrees.sort(key=lambda x: x[1], reverse=True)

    order = [v for v, _ in degrees]
    colors = [0] * n
    uncolored = set(order)
    current_color = 1

    while uncolored:
        for v in order:
            if v in uncolored:
                if all(colors[u] != current_color for u in adj[v]):
                    colors[v] = current_color
                    uncolored.remove(v)
        current_color += 1

    return colors
