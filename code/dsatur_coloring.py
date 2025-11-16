def dsatur_coloring(adj):
    n = len(adj)
    colors = [0] * n
    degrees = [len(adj[v]) for v in range(n)]
    sat = [0] * n
    uncolored = set(range(n))

    while uncolored:
        # sommet avec saturation max puis degre max
        v = max(uncolored, key=lambda x: (sat[x], degrees[x]))

        # plus petite couleur disponible
        neighbor_colors = set(colors[u] for u in adj[v] if colors[u] != 0)
        c = 1
        while c in neighbor_colors:
            c += 1
        colors[v] = c
        uncolored.remove(v)

        # mise a jour saturation
        for u in adj[v]:
            if colors[u] == 0:
                neighbor_colors_u = set(colors[w] for w in adj[u] if colors[w] != 0)
                sat[u] = len(neighbor_colors_u)

    return colors
