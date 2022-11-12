import matplotlib.pyplot     as plt
import networkx              as nx
import numpy                 as np
import sys

sys.path.append(".")
sys.path.append("..")

from seager  import Seager
from treeGen import *

np.random.seed(5)


print("Case 4 example graph. dk-1 is empty.")
tree = nx.Graph()  #Failed tree - w and z both have more than one child
tree.add_nodes_from([0, 1, 5, 6, 7, 8, 14, 15, 16, 17, 18, 19, 28, 29, 30, 31, 32, 33, 34, 35, 36])
tree.add_edges_from([
    (0, 1),
    (1, 0), (1, 5), (1, 6), (1, 7), (1, 8),
    (5, 1), (5, 14),
    (6, 1), (6, 15),
    (7, 1), (7, 16),
    (8, 1), (8, 17), (8, 18), (8, 19),
    (14, 5),
    (15, 6), (15, 28), (15, 29),
    (16, 7), (16, 30), (16, 31),
    (17, 8), (17, 32), (17, 33),
    (18, 8), (18, 34),
    (19, 8), (19, 35), (19, 36),
    (28, 15),
    (29, 15),
    (30, 16),
    (31, 16),
    (32, 17),
    (33, 17),
    (34, 18),
    (35, 19),
    (36, 19)
])

tDict = dict()
createTreeDict(tDict, tree, 0)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [16, 16, 16, 16, 16, 16], verbose = True)
solver.lemma4(1, 1, 2)
print("\n")

nx.draw(tree, with_labels = True)
plt.show()


print("Case 4 example graph. dk+1 is empty.")
tree = nx.Graph()  #Failed tree - w and z both have more than one child
tree.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 20, 21, 22, 23, 24, 25, 26, 27])
tree.add_edges_from([
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 0), (1, 5), (1, 6), (1, 7), (1, 8),
    (2, 0), (2, 9),
    (3, 0), (3, 10),
    (4, 0), (4, 11), (4, 12), (4, 13),
    (5, 1), (5, 14),
    (6, 1),
    (7, 1),
    (8, 1),
    (9, 2), (9, 20), (9, 21),
    (10, 3), (10, 22), (10, 23),
    (11, 4), (11, 24), (11, 25), 
    (12, 4), (12, 26),
    (13, 4), (13, 27),
    (14, 5),
    (20, 9),
    (21, 9),
    (22, 10),
    (23, 10),
    (24, 11),
    (25, 11),
    (26, 12),
    (27, 13),
])

tDict = dict()
createTreeDict(tDict, tree, 0)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [2, 2, 2, 2, 2], verbose = True)
solver.lemma4(1, 4, 2)
print("\n")

nx.draw(tree, with_labels = True)
plt.show()


print("Case 4 example graph. Neither dk+1 nor dk-1 are empty. d2 = 3")
tree = nx.Graph()  #Failed tree - w and z both have more than one child
tree.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36])
tree.add_edges_from([
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 0), (1, 5), (1, 6), (1, 7), (1, 8),
    (2, 0), (2, 9),
    (3, 0), (3, 10),
    (4, 0), (4, 11), (4, 12), (4, 13),
    (5, 1), (5, 14),
    (6, 1), (6, 15),
    (7, 1), (7, 16),
    (8, 1), (8, 17), (8, 18), (8, 19),
    (9, 2), (9, 20), (9, 21),
    (10, 3), (10, 22), (10, 23),
    (11, 4), (11, 24), (11, 25), 
    (12, 4), (12, 26),
    (13, 4), (13, 27),
    (14, 5),
    (15, 6), (15, 28), (15, 29),
    (16, 7), (16, 30), (16, 31),
    (17, 8), (17, 32), (17, 33),
    (18, 8), (18, 34),
    (19, 8), (19, 35), (19, 36),
    (20, 9),
    (21, 9),
    (22, 10),
    (23, 10),
    (24, 11),
    (25, 11),
    (26, 12),
    (27, 13),
    (28, 15),
    (29, 15),
    (30, 16),
    (31, 16),
    (32, 17),
    (33, 17),
    (34, 18),
    (35, 19),
    (36, 19)
])

tDict = dict()
createTreeDict(tDict, tree, 0)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [2, 2, 2, 2, 2, 2], verbose = True)
solver.lemma4(1, 4, 2)
print("\n")

nx.draw(tree, with_labels = True)
plt.show()


print("Case 4 example graph. Neither dk+1 nor dk-1 are empty. d2 = 4")
tree = nx.Graph()  #Failed tree - w and z both have more than one child
tree.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36])
tree.add_edges_from([
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 0), (1, 5), (1, 6), (1, 7), (1, 8),
    (2, 0), (2, 9),
    (3, 0), (3, 10),
    (4, 0), (4, 11), (4, 12), (4, 13),
    (5, 1), (5, 14),
    (6, 1), (6, 15),
    (7, 1), (7, 16),
    (8, 1), (8, 17), (8, 18), (8, 19),
    (9, 2), (9, 20), (9, 21),
    (10, 3), (10, 22), (10, 23),
    (11, 4), (11, 24), (11, 25), 
    (12, 4), (12, 26),
    (13, 4), (13, 27),
    (14, 5),
    (15, 6), (15, 28), (15, 29),
    (16, 7), (16, 30), (16, 31),
    (17, 8), (17, 32), (17, 33),
    (18, 8), (18, 34),
    (19, 8), (19, 35), (19, 36),
    (20, 9),
    (21, 9),
    (22, 10),
    (23, 10),
    (24, 11),
    (25, 11),
    (26, 12),
    (27, 13),
    (28, 15),
    (29, 15),
    (30, 16),
    (31, 16),
    (32, 17),
    (33, 17),
    (34, 18),
    (35, 19),
    (36, 19)
])

tDict = dict()
createTreeDict(tDict, tree, 0)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [15, 6, 6, 6, 6, 6], verbose = True)
solver.lemma4(1, 4, 2)
print("\n")

nx.draw(tree, with_labels = True)
plt.show()


print("Case 4 example graph. Neither dk+1 nor dk-1 are empty. d2 = 5")
tree = nx.Graph()  #Failed tree - w and z both have more than one child
tree.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36])
tree.add_edges_from([
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 0), (1, 5), (1, 6), (1, 7), (1, 8),
    (2, 0), (2, 9),
    (3, 0), (3, 10),
    (4, 0), (4, 11), (4, 12), (4, 13),
    (5, 1), (5, 14),
    (6, 1), (6, 15),
    (7, 1), (7, 16),
    (8, 1), (8, 17), (8, 18), (8, 19),
    (9, 2), (9, 20), (9, 21),
    (10, 3), (10, 22), (10, 23),
    (11, 4), (11, 24), (11, 25), 
    (12, 4), (12, 26),
    (13, 4), (13, 27),
    (14, 5),
    (15, 6), (15, 28), (15, 29),
    (16, 7), (16, 30), (16, 31),
    (17, 8), (17, 32), (17, 33),
    (18, 8), (18, 34),
    (19, 8), (19, 35), (19, 36),
    (20, 9),
    (21, 9),
    (22, 10),
    (23, 10),
    (24, 11),
    (25, 11),
    (26, 12),
    (27, 13),
    (28, 15),
    (29, 15),
    (30, 16),
    (31, 16),
    (32, 17),
    (33, 17),
    (34, 18),
    (35, 19),
    (36, 19)
])

tDict = dict()
createTreeDict(tDict, tree, 0)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [15, 15, 15, 15, 15, 15], verbose = True)
solver.lemma4(1, 4, 2)
print("\n")

nx.draw(tree, with_labels = True)
plt.show()


print("Case 4 example graph. Neither dk+1 nor dk-1 are empty. d2 = 6")
tree = nx.Graph()  #Failed tree - w and z both have more than one child
tree.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36])
tree.add_edges_from([
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 0), (1, 5), (1, 6), (1, 7), (1, 8),
    (2, 0), (2, 9),
    (3, 0), (3, 10),
    (4, 0), (4, 11), (4, 12), (4, 13),
    (5, 1), (5, 14),
    (6, 1), (6, 15),
    (7, 1), (7, 16),
    (8, 1), (8, 17), (8, 18), (8, 19),
    (9, 2), (9, 20), (9, 21),
    (10, 3), (10, 22), (10, 23),
    (11, 4), (11, 24), (11, 25), 
    (12, 4), (12, 26),
    (13, 4), (13, 27),
    (14, 5),
    (15, 6), (15, 28), (15, 29),
    (16, 7), (16, 30), (16, 31),
    (17, 8), (17, 32), (17, 33),
    (18, 8), (18, 34),
    (19, 8), (19, 35), (19, 36),
    (20, 9),
    (21, 9),
    (22, 10),
    (23, 10),
    (24, 11),
    (25, 11),
    (26, 12),
    (27, 13),
    (28, 15),
    (29, 15),
    (30, 16),
    (31, 16),
    (32, 17),
    (33, 17),
    (34, 18),
    (35, 19),
    (36, 19)
])

tDict = dict()
createTreeDict(tDict, tree, 0)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [15, 28, 28, 28, 28, 28], verbose = True)
solver.lemma4(1, 4, 2)
print("\n")

nx.draw(tree, with_labels = True)
plt.show()






print("Case 4 example graph. Neither dk+1 nor dk-1 are empty. d2 = 2, d3 = 2.")
tree = nx.Graph()  #Failed tree - w and z both have more than one child
tree.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36])
tree.add_edges_from([
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 0), (1, 5), (1, 6), (1, 7), (1, 8),
    (2, 0), (2, 9),
    (3, 0), (3, 10),
    (4, 0), (4, 11), (4, 12), (4, 13),
    (5, 1), (5, 14),
    (6, 1), (6, 15),
    (7, 1), (7, 16),
    (8, 1), (8, 17), (8, 18), (8, 19),
    (9, 2), (9, 20), (9, 21),
    (10, 3), (10, 22), (10, 23),
    (11, 4), (11, 24), (11, 25), 
    (12, 4), (12, 26),
    (13, 4), (13, 27),
    (14, 5),
    (15, 6), (15, 28), (15, 29),
    (16, 7), (16, 30), (16, 31),
    (17, 8), (17, 32), (17, 33),
    (18, 8), (18, 34),
    (19, 8), (19, 35), (19, 36),
    (20, 9),
    (21, 9),
    (22, 10),
    (23, 10),
    (24, 11),
    (25, 11),
    (26, 12),
    (27, 13),
    (28, 15),
    (29, 15),
    (30, 16),
    (31, 16),
    (32, 17),
    (33, 17),
    (34, 18),
    (35, 19),
    (36, 19)
])

tDict = dict()
createTreeDict(tDict, tree, 0)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [2, 0, 2, 2, 2, 2], verbose = True)
solver.lemma4(1, 4, 2)
print("\n")

nx.draw(tree, with_labels = True)
plt.show()


print("Case 4 example graph. Neither dk+1 nor dk-1 are empty. d2 = 2, d3 = 3.")
tree = nx.Graph()  #Failed tree - w and z both have more than one child
tree.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36])
tree.add_edges_from([
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 0), (1, 5), (1, 6), (1, 7), (1, 8),
    (2, 0), (2, 9),
    (3, 0), (3, 10),
    (4, 0), (4, 11), (4, 12), (4, 13),
    (5, 1), (5, 14),
    (6, 1), (6, 15),
    (7, 1), (7, 16),
    (8, 1), (8, 17), (8, 18), (8, 19),
    (9, 2), (9, 20), (9, 21),
    (10, 3), (10, 22), (10, 23),
    (11, 4), (11, 24), (11, 25), 
    (12, 4), (12, 26),
    (13, 4), (13, 27),
    (14, 5),
    (15, 6), (15, 28), (15, 29),
    (16, 7), (16, 30), (16, 31),
    (17, 8), (17, 32), (17, 33),
    (18, 8), (18, 34),
    (19, 8), (19, 35), (19, 36),
    (20, 9),
    (21, 9),
    (22, 10),
    (23, 10),
    (24, 11),
    (25, 11),
    (26, 12),
    (27, 13),
    (28, 15),
    (29, 15),
    (30, 16),
    (31, 16),
    (32, 17),
    (33, 17),
    (34, 18),
    (35, 19),
    (36, 19)
])

tDict = dict()
createTreeDict(tDict, tree, 0)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [4, 12, 12, 12, 12, 12], verbose = True)
solver.lemma4(1, 4, 2)
print("\n")

nx.draw(tree, with_labels = True)
plt.show()


print("Case 4 example graph. Neither dk+1 nor dk-1 are empty. d2 = 2, d3 = 4.")
tree = nx.Graph()  #Failed tree - w and z both have more than one child
tree.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36])
tree.add_edges_from([
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 0), (1, 5), (1, 6), (1, 7), (1, 8),
    (2, 0), (2, 9),
    (3, 0), (3, 10),
    (4, 0), (4, 11), (4, 12), (4, 13),
    (5, 1), (5, 14),
    (6, 1), (6, 15),
    (7, 1), (7, 16),
    (8, 1), (8, 17), (8, 18), (8, 19),
    (9, 2), (9, 20), (9, 21),
    (10, 3), (10, 22), (10, 23),
    (11, 4), (11, 24), (11, 25), 
    (12, 4), (12, 26),
    (13, 4), (13, 27),
    (14, 5),
    (15, 6), (15, 28), (15, 29),
    (16, 7), (16, 30), (16, 31),
    (17, 8), (17, 32), (17, 33),
    (18, 8), (18, 34),
    (19, 8), (19, 35), (19, 36),
    (20, 9),
    (21, 9),
    (22, 10),
    (23, 10),
    (24, 11),
    (25, 11),
    (26, 12),
    (27, 13),
    (28, 15),
    (29, 15),
    (30, 16),
    (31, 16),
    (32, 17),
    (33, 17),
    (34, 18),
    (35, 19),
    (36, 19)
])

tDict = dict()
createTreeDict(tDict, tree, 0)
lDict = createLevelsDict(tDict)

solver = Seager(tree, tDict, lDict, [4, 12, 26, 26, 26, 26], verbose = True)
solver.lemma4(1, 4, 2)
print("\n")

nx.draw(tree, with_labels = True)
plt.show()
