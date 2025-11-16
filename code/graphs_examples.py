# graphs_examples.py

GRAPHS = {
    "Cycle C5": [
        [1,4],
        [0,2],
        [1,3],
        [2,4],
        [3,0]
    ],

    "Cycle C6": [
        [1,5],
        [0,2],
        [1,3],
        [2,4],
        [3,5],
        [4,0]
    ],

    "Graphe complet K4": [
        [1,2,3],
        [0,2,3],
        [0,1,3],
        [0,1,2]
    ],

    "Biparti K3,3": [
        [3,4,5],
        [3,4,5],
        [3,4,5],
        [0,1,2],
        [0,1,2],
        [0,1,2]
    ],

    "Graphe de Petersen": [
        [1,4,5],
        [0,2,6],
        [1,3,7],
        [2,4,8],
        [3,0,9],
        [0,7,8],
        [1,8,9],
        [2,5,9],
        [3,5,6],
        [4,6,7]
    ],

    # Exemple simple : 4 departements voisins
    "Graphe Departements (4 regions)": [
        [1,2],   # Region 0 touche 1 et 2
        [0,2,3], # Region 1 touche 0,2,3
        [0,1,3], # Region 2 touche 0,1,3
        [1,2]    # Region 3 touche 1,2
    ]
}
