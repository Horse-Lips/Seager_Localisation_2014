import matplotlib.pyplot     as plt
import networkx              as nx
import numpy                 as np
import sys

sys.path.append(".")
sys.path.append("..")

from seager  import Seager
from treeGen import *

np.random.seed(5)


print("Case 1 example graph. vk-1 (node 1) has only one child, vk.")
tree = nx.Graph()  #Failed tree - w and z both have more than one child
tree.add_nodes_from([0, 1, 2, 6, 7, 8, 9, 10, 11, 12, 13, 14])
tree.add_edges_from([
    (0,  1),
    (1,  0), (1, 2),
    (2,  1), (2, 6),  (2, 7), (2, 8), (2, 9),
    (6,  2), (6, 10), (6, 11),
    (7,  2), (7, 12),
    (8,  2), (8, 13),
    (9,  2), (9, 14),
    (10, 6),
    (11, 6),
    (12, 7),
    (13, 8),
    (14, 9)
])

tDict = dict()
createTreeDict(tDict, tree, 0)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [9], verbose = True)
solver.solve()
print("\n")

nx.draw(tree, with_labels = True)
plt.show()


print("Case 1 example graph. vk-1 has more than one child, zk has at most one child, d2 = 2.")
tree = nx.Graph()  #Failed tree - w and z both have more than one child
tree.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
tree.add_edges_from([
    (0,  1),
    (1,  0), (1, 2),  (1, 3), (1, 4), (1, 5),
    (2,  1), (2, 6),  (2, 7), (2, 8), (2, 9),
    (3,  1),
    (4,  1),
    (5,  1),
    (6,  2), (6, 10), (6, 11),
    (7,  2), (7, 12),
    (8,  2), (8, 13),
    (9,  2), (9, 14),
    (10, 6),
    (11, 6),
    (12, 7),
    (13, 8),
    (14, 9)
])

tDict = dict()
createTreeDict(tDict, tree, 0)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [1, 3, 3, 3, 3], verbose = True)
solver.solve()
print("\n")

np.random.seed(5)
nx.draw(tree, with_labels = True)
plt.show()


print("Case 1 example graph. vk-1 has more than one child, zk has at most one child, d2 = 3.")
tree = nx.Graph()  #Failed tree - w and z both have more than one child
tree.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
tree.add_edges_from([
    (0,  1),
    (1,  0), (1, 2),  (1, 3), (1, 4), (1, 5),
    (2,  1), (2, 6),  (2, 7), (2, 8), (2, 9),
    (3,  1),
    (4,  1),
    (5,  1),
    (6,  2), (6, 10), (6, 11),
    (7,  2), (7, 12),
    (8,  2), (8, 13),
    (9,  2), (9, 14),
    (10, 6),
    (11, 6),
    (12, 7),
    (13, 8),
    (14, 9)
])

tDict = dict()
createTreeDict(tDict, tree, 0)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [7, 7, 7, 7, 7], verbose = True)
solver.solve()
print("\n")

np.random.seed(5)
nx.draw(tree, with_labels = True)
plt.show()


print("Case 1 example graph. vk-1 has more than one child, zk has at most one child, d2 = 4.")
tree = nx.Graph()  #Failed tree - w and z both have more than one child
tree.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
tree.add_edges_from([
    (0,  1),
    (1,  0), (1, 2),  (1, 3), (1, 4), (1, 5),
    (2,  1), (2, 6),  (2, 7), (2, 8), (2, 9),
    (3,  1),
    (4,  1),
    (5,  1),
    (6,  2), (6, 10), (6, 11),
    (7,  2), (7, 12),
    (8,  2), (8, 13),
    (9,  2), (9, 14),
    (10, 6),
    (11, 6),
    (12, 7),
    (13, 8),
    (14, 9)
])

tDict = dict()
createTreeDict(tDict, tree, 0)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [7, 12, 12, 12, 12, 12], verbose = True)
solver.solve()
print("\n")

np.random.seed(5)
nx.draw(tree, with_labels = True)
plt.show()


print("Case 1 example graph. vk-1 has more than one child, zk has more than one child, d2 = 2.")
tree = nx.Graph()  #Failed tree - w and z both have more than one child
tree.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
tree.add_edges_from([
    (0,  1),
    (1,  0), (1, 2),  (1, 3), (1, 4), (1, 5),
    (2,  1), (2, 6),  (2, 7), (2, 8), (2, 9),
    (3,  1),
    (4,  1),
    (5,  1), (5, 15), (5, 16),
    (6,  2), (6, 10), (6, 11),
    (7,  2), (7, 12),
    (8,  2), (8, 13),
    (9,  2), (9, 14),
    (10, 6),
    (11, 6),
    (12, 7),
    (13, 8),
    (14, 9),
    (15, 5),
    (16, 5)
])

tDict = dict()
createTreeDict(tDict, tree, 0)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [1, 4, 4, 4, 4, 4], verbose = True)
solver.solve()
print("\n")

np.random.seed(5)
nx.draw(tree, with_labels = True)
plt.show()


print("Case 1 example graph. vk-1 has more than one child, zk has more than one child, d2 = 3.")
tree = nx.Graph()  #Failed tree - w and z both have more than one child
tree.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
tree.add_edges_from([
    (0,  1),
    (1,  0), (1, 2),  (1, 3), (1, 4), (1, 5),
    (2,  1), (2, 6),  (2, 7), (2, 8), (2, 9),
    (3,  1),
    (4,  1),
    (5,  1), (5, 15), (5, 16),
    (6,  2), (6, 10), (6, 11),
    (7,  2), (7, 12),
    (8,  2), (8, 13),
    (9,  2), (9, 14),
    (10, 6),
    (11, 6),
    (12, 7),
    (13, 8),
    (14, 9),
    (15, 5),
    (16, 5)
])

tDict = dict()
createTreeDict(tDict, tree, 0)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [9, 9, 9, 9, 9, 9], verbose = True)
solver.solve()
print("\n")

np.random.seed(5)
nx.draw(tree, with_labels = True)
plt.show()


print("Case 1 example graph. vk-1 has more than one child, zk has more than one child, d2 = 4.")
tree = nx.Graph()  #Failed tree - w and z both have more than one child
tree.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
tree.add_edges_from([
    (0,  1),
    (1,  0), (1, 2),  (1, 3), (1, 4), (1, 5),
    (2,  1), (2, 6),  (2, 7), (2, 8), (2, 9),
    (3,  1),
    (4,  1),
    (5,  1), (5, 15), (5, 16),
    (6,  2), (6, 10), (6, 11),
    (7,  2), (7, 12),
    (8,  2), (8, 13),
    (9,  2), (9, 14),
    (10, 6),
    (11, 6),
    (12, 7),
    (13, 8),
    (14, 9),
    (15, 5),
    (16, 5)
])

tDict = dict()
createTreeDict(tDict, tree, 0)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [7, 12, 12, 12, 12, 12], verbose = True)
solver.solve()
print("\n")

np.random.seed(5)
nx.draw(tree, with_labels = True)
plt.show()
