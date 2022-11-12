import matplotlib.pyplot     as plt
import networkx              as nx
import sys

sys.path.append(".")
sys.path.append("..")

from seager  import Seager
from treeGen import *


tree = nx.Graph()
tree.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
tree.add_edges_from([(0, 1), (0, 2), (0, 3), (1, 0), (1, 4), (1, 5), (2, 0), (2, 6), (2, 7), (3, 0), (3, 8), (3, 9), (4, 1), (5, 1), (6, 2), (7, 2), (8, 3), (9, 3)])

tDict = dict()
createTreeDict(tDict, tree, 0)      #Create treeDict representation hideout
lDict = createLevelsDict(tDict)    #Create levelsDict representation

solver = Seager(tree, tDict, lDict, [0], verbose = True)    #Create solver instance for hideout
solver.solve()

nx.draw(tree, with_labels = True)
plt.show()
