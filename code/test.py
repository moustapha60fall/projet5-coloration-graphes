from backtracking_coloration import exact_k_coloring
from greedy import greedy_coloring
from welsh_powell import welsh_powell
from dsatur_coloring import dsatur_coloring

# exemple : C5
adj_C5 = {
    0: [1,4],
    1: [0,2],
    2: [1,3],
    3: [2,4],
    4: [3,0]
}
adj_list_C5 = [adj_C5[i] for i in range(5)]

print("Backtracking k=3:", exact_k_coloring(adj_list_C5, 3))
print("Greedy:", greedy_coloring(adj_list_C5))
print("Welsh-Powell:", welsh_powell(adj_list_C5))
print("DSATUR:", dsatur_coloring(adj_list_C5))
