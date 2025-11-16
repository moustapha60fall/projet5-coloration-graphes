# run_all_tests.py
from backtracking_coloration import exact_k_coloring
from greedy import greedy_coloring
from welsh_powell import welsh_powell
from dsatur_coloring import dsatur_coloring

from visualization import visualize_coloring
from pretty_draw import visualize_pretty
from graphs_examples import GRAPHS


def run_tests():
    for name, adj in GRAPHS.items():
        print("\n==============================")
        print(" Graphe :", name)
        print("==============================")

        # ---- BACKTRACKING ----
        print("\nBacktracking (k=3) :")
        colors_bt = exact_k_coloring(adj, 3)
        print(colors_bt)
        if colors_bt:
            visualize_coloring(adj, colors_bt, f"Backtracking (k=3) – {name}")
            visualize_pretty(adj, colors_bt, f"Pretty Backtracking – {name}")
        else:
            print("Aucune coloration trouvée avec k=3.")

        # ---- GREEDY ----
        print("\nGreedy Coloring :")
        colors_g = greedy_coloring(adj)
        print(colors_g)
        visualize_coloring(adj, colors_g, f"Greedy – {name}")
        visualize_pretty(adj, colors_g, f"Pretty Greedy – {name}")

        # ---- WELSH–POWELL ----
        print("\nWelsh–Powell :")
        colors_wp = welsh_powell(adj)
        print(colors_wp)
        visualize_coloring(adj, colors_wp, f"Welsh–Powell – {name}")
        visualize_pretty(adj, colors_wp, f"Pretty Welsh–Powell – {name}")

        # ---- DSATUR ----
        print("\nDSATUR :")
        colors_ds = dsatur_coloring(adj)
        print(colors_ds)
        visualize_coloring(adj, colors_ds, f"DSATUR – {name}")
        visualize_pretty(adj, colors_ds, f"Pretty DSATUR – {name}")


if __name__ == "__main__":
    run_tests()
