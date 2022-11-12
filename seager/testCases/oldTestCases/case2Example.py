import matplotlib.pyplot     as plt
import networkx              as nx
import numpy                 as np
import sys

sys.path.append(".")
sys.path.append("..")

from seager  import Seager
from treeGen import *

np.random.seed(5)


print("Case 2 example graph.")
tree = nx.Graph()  #Failed tree - w and z both have more than one child
tree.add_nodes_from([0, 1, 2, 6, 7, 8, 9, 10, 11, 12])
tree.add_edges_from([
    (0,  1),
    (1,  0), (1, 2), (1, 3), (1, 4), (1, 5),
    (2,  1), (2, 6), (2, 7),
    (3,  1), (3, 8),
    (4,  1), (4, 9),
    (5,  1), (5, 10), (5, 11), (5, 12),
    (6,  2),
    (7,  2),
    (8,  3),
    (9,  4),
    (10, 5),
    (11, 5),
    (12, 5)
])

tDict = dict()
createTreeDict(tDict, tree, 0)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [5, 5, 5, 5, 5, 5], verbose = True)
solver.lemma4(1, 1, 2)
print("\n")

nx.draw(tree, with_labels = True)
plt.show()


print("Case 2 example graph. vk has no children.")
tree = nx.Graph()  #Failed tree - w and z both have more than one child
tree.add_nodes_from([0, 1, 2, 8, 9, 10, 11, 12])
tree.add_edges_from([
    (0,  1),
    (1,  0), (1, 2), (1, 3), (1, 4), (1, 5),
    (2,  1),
    (3,  1), (3, 8),
    (4,  1), (4, 9),
    (5,  1), (5, 10), (5, 11), (5, 12),
    (8,  3),
    (9,  4),
    (10, 5),
    (11, 5),
    (12, 5)
])

tDict = dict()
createTreeDict(tDict, tree, 0)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [5, 5, 5, 5, 5, 5], verbose = True)
solver.lemma4(1, 1, 2)
print("\n")

nx.draw(tree, with_labels = True)
plt.show()
