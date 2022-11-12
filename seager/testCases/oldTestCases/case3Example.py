import matplotlib.pyplot     as plt
import networkx              as nx
import numpy                 as np
import sys

sys.path.append(".")
sys.path.append("..")

from seager  import Seager
from treeGen import *

np.random.seed(5)


print("Case 3 example graph.")
tree = nx.Graph()  #Failed tree - w and z both have more than one child
tree.add_nodes_from([0, 1, 2, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
tree.add_edges_from([
    (0, 1), (0, 2), (0, 3), (0,  4),
    (1, 0), (1, 5),
    (2, 0), (2, 6),
    (3, 0), (3, 7),
    (4, 0), (4, 8), (4, 9), (4, 10),
    (5, 1), (5, 11),
    (6, 2), (6, 12), (6, 13),
    (7, 3), (7, 14), (7, 15),
    (8, 4), (8, 16), (8, 17),
    (9, 4), (9, 18),
    (10, 4), (10, 19), (10, 20),
    (11, 5), (11, 21),
    (12, 6),
    (13, 6),
    (14, 7),
    (15, 7),
    (16, 8),
    (17, 8),
    (18, 9),
    (19, 10),
    (20, 10),
    (21, 11)
])

tDict = dict()
createTreeDict(tDict, tree, 0)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [13, 13, 13, 13, 13, 13], verbose = True)
solver.lemma4(5, 10, 3)
print("\n")

nx.draw(tree, with_labels = True)
plt.show()
