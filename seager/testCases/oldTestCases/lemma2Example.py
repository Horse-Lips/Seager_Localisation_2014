import matplotlib.pyplot     as plt
import networkx              as nx
import numpy                 as np
import sys

sys.path.append(".")
sys.path.append("..")

from seager  import Seager
from treeGen import *

np.random.seed(5)


print("Failed tree, w and z both have more than one child.")
tree = nx.Graph()
tree.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
tree.add_edges_from([
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 0), (1, 5), (1, 9),
    (2, 0), (2, 6),
    (3, 0), (3, 7),
    (4, 0), (4, 8), (4, 10),
    (5, 1),
    (6, 2),
    (7, 3),
    (8, 4),
    (9, 1),
    (10, 4)
])

tDict = dict()
createTreeDict(tDict, tree, 0)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [0], verbose = True)
solver.lemma2(0, 1, 4)
print("\n")

nx.draw(tree, with_labels = True)
plt.show()


print("Successful tree, each child of v has exactly one child.")
tree = nx.Graph() #Successful tree - Each child of the root has exactly one child
tree.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8])
tree.add_edges_from([
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 0), (1, 5),
    (2, 0), (2, 6),
    (3, 0), (3, 7),
    (4, 0), (4, 8),
    (5, 1),
    (6, 2),
    (7, 3),
    (8, 4)
])

tDict = dict()
createTreeDict(tDict, tree, 0)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [4], verbose = True)
solver.lemma2(0, 1, 4)
print("\n")

nx.draw(tree, with_labels = True)
plt.show()


print("Sucessful tree, only z has more than one child.")
tree = nx.Graph() #Successful tree - z has two children
tree.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
tree.add_edges_from([
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 0), (1, 5),
    (2, 0), (2, 6),
    (3, 0), (3, 7),
    (4, 0), (4, 8), (4, 9),
    (5, 1),
    (6, 2),
    (7, 3),
    (8, 4),
    (9, 4)
])

tDict = dict()
createTreeDict(tDict, tree, 0)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [4], verbose = True)
solver.lemma2(0, 1, 4)
print("\n")

nx.draw(tree, with_labels = True)
plt.show()


print("Successful tree, only w has more than one child.")
tree = nx.Graph()
tree.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
tree.add_edges_from([
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 0), (1, 5), (1, 9),
    (2, 0), (2, 6),
    (3, 0), (3, 7),
    (4, 0), (4, 8),
    (5, 1),
    (6, 2),
    (7, 3),
    (8, 4),
    (9, 1)
])

tDict = dict()
createTreeDict(tDict, tree, 0)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [1], verbose = True)
solver.lemma2(0, 1, 4)
print("\n")

nx.draw(tree, with_labels = True)
plt.show()


print("Successful tree, node 3 has no children.")
tree = nx.Graph()
tree.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 8])
tree.add_edges_from([
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 0), (1, 5),
    (2, 0), (2, 6),
    (3, 0),
    (4, 0),
    (4, 8),
    (5, 1),
    (6, 2),
    (8, 4)
])

tDict = dict()
createTreeDict(tDict, tree, 0)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [4], verbose = True)
solver.lemma2(0, 1, 4)
print("\n")


nx.draw(tree, with_labels = True)
plt.show()


print("Successful tree, target moves to children of z.")
tree = nx.Graph()
tree.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
tree.add_edges_from([
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 0), (1, 5),
    (2, 0), (2, 6),
    (3, 0), (3, 7),
    (4, 0), (4, 8), (4, 9),
    (5, 1),
    (6, 2),
    (7, 3),
    (8, 4),
    (9, 4)
])

tDict = dict()
createTreeDict(tDict, tree, 0)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [4, 4, 8, 8], verbose = True)
solver.lemma2(0, 1, 4)
print("\n")

nx.draw(tree, with_labels = True)
plt.show()
