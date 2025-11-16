# Projet 5 : Coloration de graphes

## Description
Ce projet fait partie du module **Complexité Algébrique** à l’Université Cheikh Anta Diop de Dakar (UCAD).  
Il porte sur l’implémentation et l’analyse de plusieurs algorithmes classiques de **coloration de graphes**, un problème fondamental en théorie des graphes et reconnu comme NP-difficile.

Le rapport associé est rédigé en **LaTeX** et présente :
- Les définitions et bases théoriques.
- L’implémentation en **Python** de plusieurs algorithmes.
- L’analyse de leur complexité théorique et expérimentale.
- Les preuves de correction.
- Des applications pratiques (planification d’examens, allocation de registres, attribution de fréquences radio, Sudoku, etc.).

---

## Algorithmes implémentés
- **Backtracking (exact)** : exploration exhaustive, solution optimale mais coûteuse.
- **Glouton (Greedy)** : rapide, dépend de l’ordre des sommets.
- **Welsh–Powell** : amélioration du glouton par tri des sommets.
- **DSATUR** : heuristique avancée basée sur la saturation, proche de l’optimal.

---

## Modules Python nécessaires
Le projet utilise principalement :
- `networkx` : manipulation de graphes.
- `matplotlib` : visualisation des graphes.
- `random` : génération de graphes aléatoires.
- `time` : mesure des performances.

---

## Exécution
1. Cloner le dépôt :
   ```bash
   git clone https://github.com/moustapha60fall/projet5-coloration-graphes
   cd projet5-coloration-graphes/code
