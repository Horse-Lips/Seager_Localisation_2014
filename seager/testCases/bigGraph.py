import networkx as nx
import sys

sys.path.append("../..")
from seager import Seager


tree = nx.Graph()
tree.add_nodes_from(range(102))
edges = [
    (0, 1),
    (1, 2), (1, 3), (1, 4), 
    (2, 5), (2, 6), (2, 7), 
    (3, 8), 
    (4, 9), (4, 10), 
    (5, 11), (5, 12), 
    (6, 13), 
    (7, 14), 
    (9, 15), (9, 16), 
    (10, 17), (10, 18),
    (11, 19), (11, 20), 
    (13, 21), (13, 22), (13, 23), 
    (15, 24), 
    (16, 25), 
    (17, 26), (17, 27), (17, 28), 
    (19, 29), (19, 30), 
    (20, 31), 
    (21, 32), 
    (22, 33), 
    (23, 34), 
    (24, 35), (24, 36), 
    (25, 37), (25, 38), 
    (26, 39), 
    (29, 40), 
    (30, 41), 
    (31, 42), 
    (32, 43), 
    (33, 44), (33, 45), 
    (34, 46), (34, 47), 
    (37, 48), (37, 49), 
    (38, 50),
    (39, 51), (39, 52), (39, 53),
    (40, 54), (40, 55), 
    (41, 56), 
    (42, 57), 
    (44, 58), (44, 59), 
    (45, 60), 
    (46, 61), (46, 62), (46, 63), 
    (50, 64), (50, 65), 
    (51, 66), (51, 67), 
    (53, 68), (53, 69), 
    (54, 70), (54, 71), (54, 72), (54, 73), 
    (58, 74), (58, 75), (58, 76), 
    (60, 77), 
    (61, 78), (61, 79), (61, 80), 
    (66, 81), (66, 82), (66, 83), 
    (67, 84), 
    (68, 85), 
    (70, 86), (70, 87), (70, 88), 
    (73, 89), 
    (74, 90), (74, 91), 
    (76, 92), 
    (77, 93), (77, 94), (77, 95), 
    (78, 96), 
    (80, 97), 
    (81, 98), (81, 99), 
    (83, 100), 
    (85, 101), 
]

for edge in edges:
    tree.add_edge(edge[0], edge[1])
    tree.add_edge(edge[1], edge[0])


successful = 0

for i in range(0, len(tree)):
    solver = Seager(tree)
    solver["t"] = [i]
    solver.solve()

    if solver["tLocation"] == solver["t"][-1]:
        successful += 1

    else:
        print("====== Initial Target Location:", i, "======")
        print(solver["trace"])
        print("Target list:",     solver["t"])
        print("Probe list:",      solver["probeList"])
        print("Located at node:", solver["tLocation"])
        print("\n")

print("Execution finished.")
print(successful, "/", len(tree), "successful")

