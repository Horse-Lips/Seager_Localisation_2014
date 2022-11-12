import matplotlib.pyplot     as plt
import networkx              as nx
import numpy                 as np
import sys

sys.path.append(".")
sys.path.append("..")

from seager  import Seager
from treeGen import *

np.random.seed(5)


print("Failed tree where v has parent u, w and z both have more than one child.")
tree = nx.Graph()  #Failed tree - w and z both have more than one child
tree.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
tree.add_edges_from([(11, 0), (0, 11), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 5), (1, 9), (2, 0), (2, 6), (3, 0), (3, 7), (4, 0), (4, 8), (4, 10), (5, 1), (6, 2), (7, 3), (8, 4), (9, 1), (10, 4)])

tDict = dict()
createTreeDict(tDict, tree, 11)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [4], verbose = True)
solver.lemma3(11, 0, 1, 4)
print("\n")

nx.draw(tree, with_labels = True)
plt.show()


print("Failed tree where v has parent u which has parent u', w and z both have more than one child.")
tree = nx.Graph()  #Failed tree - w and z both have more than one child
tree.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
tree.add_edges_from([(12, 11), (11, 12), (11, 0), (0, 11), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 5), (1, 9), (2, 0), (2, 6), (3, 0), (3, 7), (4, 0), (4, 8), (4, 10), (5, 1), (6, 2), (7, 3), (8, 4), (9, 1), (10, 4)])

tDict = dict()
createTreeDict(tDict, tree, 12)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [4], verbose = True)
solver.lemma3(11, 0, 1, 4)
print("\n")


nx.draw(tree, with_labels = True)
plt.show()


print("Successful tree, each child of v has exactly one child.")
tree = nx.Graph() #Successful tree - Each child of the root has exactly one child
tree.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
tree.add_edges_from([(10, 9), (9, 10), (9, 0), (0, 9), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 5), (2, 0), (2, 6), (3, 0), (3, 7), (4, 0), (4, 8), (5, 1), (6, 2), (7, 3), (8, 4)])

tDict = dict()
createTreeDict(tDict, tree, 10)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [4], verbose = True)
solver.lemma3(9, 0, 1, 4)
print("\n")

nx.draw(tree, with_labels = True)
plt.show()
