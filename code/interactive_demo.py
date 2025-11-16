import networkx as nx
import matplotlib.pyplot as plt
from ipywidgets import interact, Dropdown

from backtracking_coloration import exact_k_coloring
from greedy import greedy_coloring
from welsh_powell import welsh_powell
from dsatur_coloring import dsatur_coloring

from graphs_examples import GRAPHS
from visualization import visualize_coloring

def interactive_coloring(graph_name, algo_name):
    adj = GRAPHS[graph_name]

    if algo_name == "Backtracking (k=3)":
        colors = exact_k_coloring(adj, 3)
    elif algo_name == "Greedy":
        colors = greedy_coloring(adj)
    elif algo_name == "Welsh–Powell":
        colors = welsh_powell(adj)
    else:
        colors = dsatur_coloring(adj)

    visualize_coloring(adj, colors, f"{algo_name} on {graph_name}")

interact(
    interactive_coloring,
    graph_name=Dropdown(options=list(GRAPHS.keys()), description="Graphe:"),
    algo_name=Dropdown(options=["Backtracking (k=3)", "Greedy", "Welsh–Powell", "DSATUR"], description="Algorithme:")
)
