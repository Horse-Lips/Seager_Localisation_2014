import sys
import networkx as nx
import numpy    as np

from random   import choice
from ._utils  import located, reduceSet, children
from ._lemma1 import lemma1
from ._lemma2 import lemma2
from ._case1  import case1
from ._case2  import case2
from ._case3  import case3
from ._case4  import case4
from ._case5  import case5


class Seager:
    def __init__(self, tree, t, verbose = False):
        self.tree  = tree   #NetworkX tree object (Rooted at node 0)
        self.tDict = dict() #Dict representation of tree object (See createTreeDict)  
        self.lDict = dict() #Dict of level information of the tree object (See createLevelsDict)

        self.probeNum   = 0     #The number of the probe for list indexing
        self.k          = 0     #Level marked as k in the tree
        self.dkMinus, self.dk, self.dkPlus = [], [], [] #Target locations on levels k - 1, k, and k + 1

        self.verbose = verbose   #Output useful information during execution

        self.l  = 0 #Highest level path P can reach from probe p to target location t
        self.vl, self.yl, self.zl = 0, 0, 0 #v, y, and z's ancestors on level l, used in case 5

        self.probeList = [0]    #List of probed nodes
        self.t         = t      #List of nodes target occupied
        self.tLocation = -1     #Node target was located at

        self.createTreeDict(0)  #Initialise the tree dict
        self.createLevelsDict() #Initialise the levels dict


    def solve(self):
        """
         - Carries out the strategy of theorem 8. Firstly the
         - root of the tree is probed, then Lemma 4 is called.
        """
        if lemma1(self) == -1:  #Organise tree and check for hideouts
            return None         #Exit if hideout detected

        print(self.tDict[self.tDict[27].parent].children)

        d = nx.shortest_path_length(self.tree, self.lDict[0][0], self.t[self.probeNum])   #Probe root
        self.probeNum += 1

        if d == 0:
            return located(self, self.lDict[0][0])

        elif len(self.lDict[d]) == 1:
            return located(self, self.lDict[d][0])

        self.lemma4(self.tDict[self.lDict[d][0]].parent, self.tDict[self.lDict[d][-1]].parent, d)
        return


    def lemma4(self, w, z, k):
        """
         - Applies lemma 4 which, when the target set is contained
         - in Children(w, z) with w and z on the same level with
         - w <= z, finds w' and z' on the same level with w' <= z'
         - such that the target set is contained in Children(w', z').
         - F(Children(w', z')) is a strict subset of F(Children(w, z)).
         - Args:
            - w - The leftmost sibling of Siblings(w, z).
            - z - The rightmost sibling of Siblings(w, z).
            - k - The level in the tree of Children(w, z) (NOT w and z).
        """
        print("Lemma 4 called for Children(", w, ",", z, ") on level", k) if self.verbose else None

        if w == z and self.tDict[w].children == []:
            return located(self, w)

        self.dkMinus = []
        self.dk      = children(self, w, z)
        self.dkPlus  = []
        self.k = k                          #Set global value of level k
        self.expandDSets()

        w, z   = reduceSet(self, w, z)      #Replace w with w', z with z' if no children
        vk     = self.tDict[w].children[0]  #Let vk be the first child of w
        print("Assigned vk to node:", vk) if self.verbose else None

        if len(children(self, w, z)) == 1:
            return located(self, children(self, w, z)[0])
            

        p, d = (vk, 1) if len(self.tDict[vk].children) == 0 else (self.tDict[vk].children[0], 0)
        d1   = self.probe(p)

        ds = self.updateDSets(p, d1)

        if ds != -1:
            print("located by dist set update")
            return

        elif d1 == 0:
            return located(self, p)

        elif d1 == 1:
            return located(self, self.tDict[p].parent)

        elif d1 == 2:
            if d:   #If probed vk and d1 == 2 then lemma 2 w's other children
                lemma2(self, w, self.dk[0], self.dk[-1])
                return

            elif w == z and len(self.tDict[vk].children) == 1:
                print("Located here!!!")
                return located(self, w)

            else:
                case1(self, p, w, d1, k)
                return

        elif d1 == 3:
            if d:   #If probed vk and d1 == 3 then case 4 (dk-1 and dk+1 non-empty)
                case4(self, p, w, d1, k)
                return

            case2(self, p, w, d1, k)
            return

        elif d1 == 4:
            if d:   #If probed vk and d1 == 4 then target in subset of Children(w, z)
                self.lemma4(self.tDict[self.dk[0]].parent, self.tDict[self.dk[-1]].parent, k)
                return

            case4(self, p, w, d1, k)
            return

        elif d1 % 2 == 1 and d1 > 3:
            if d:   #If vk probed then dk+1 and dk-1 possible
                if self.dkMinus == []:
                    self.lemma4(self.tDict[self.dkPlus[0]].parent, self.tDict[self.dkPlus[-1]].parent, self.k + 1)
                    return

                elif self.dkPlus == []:
                    self.lemma4(self.tDict[self.dkMinus[0]].parent, self.tDict[self.dkMinus[-1]].parent, self.k - 1)
                    return

            case3(self, p, w, d1, k)
            return

        elif d1 % 2 == 0 and d1 > 5:
            if d:
                self.lemma4(self.tDict[self.dk[0]].parent, self.tDict[self.dk[-1]].parent, k)
                return

            if self.dkMinus == []:
                self.lemma4(self.tDict[self.dkPlus[0]].parent, self.tDict[self.dkPlus[-1]].parent, k + 1)
                return

            elif self.dkPlus == []:
                self.lemma4(self.tDict[self.dkMinus[0]].parent, self.tDict[self.dkMinus[-1]].parent, k - 1)
                return

            else:
                case5(self, p, w, d1, self.dkMinus[-1])
                return


    def probe(self, v):
        """
         - Returns the distance from v to the target
        """
        self.probeList.append(v)

        if self.probeNum == len(self.t):    #Move target randomly if the target move set is empty
            self.t.append(choice([i for i in self.tree.neighbors(self.t[-1])]))

        self.probeNum += 1

        d  = nx.shortest_path_length(self.tree, v, self.t[self.probeNum - 1])

        print("Probing node:", v, "for target at node", self.t[self.probeNum - 1], "and d =", d) if self.verbose else None
        
        return d

        
    def updateDSets(self, v, d):
        """
         - Updates the sets Dk-1, Dk, Dk+1
        """
        distances = nx.single_source_dijkstra_path_length(self.tree, v)
        dkMinus, dk, dkPlus = [], [], []

        tSet = self.dkMinus + self.dk + self.dkPlus

        print(self.dkMinus, self.dk, self.dkPlus)
        print(tSet)

        for i in distances:
            if distances[i] == d and i in tSet:
                print(i, ",", self.tDict[i].level)
                print("k =", self.k)

                if self.tDict[i].level == self.k - 1:
                    dkMinus.append(i)

                elif self.tDict[i].level == self.k:
                    dk.append(i)


                elif self.tDict[i].level == self.k + 1:
                    dkPlus.append(i)

        print(dkMinus, dk, dkPlus)

        tSetNew = dkMinus + dk + dkPlus

        if len(tSetNew) == 1:
            return located(self, tSetNew[0])

        self.dkMinus = dkMinus
        self.dk      = dk
        self.dkPlus  = dkPlus

        return -1


    def expandDSets(self):
        """
         - Expands Dk-1, Dk, and Dk+1 simulating target movement
        """
        for n in self.dk:
            if self.tDict[n].parent not in self.dkMinus:
                self.dkMinus.append(self.tDict[n].parent)

            for c in self.tDict[n].children:
                if c not in self.dkPlus:
                    self.dkPlus.append(c)


    def createTreeDict(self, node, parent = None, level = 0):
        """
         - Converts a tree to a dictionary, where keys are the
         - the node's ID and values are nodeInfo entries as above.
         - Args:
            - d      - A dictionary.
            - tree   - A networkx tree.
            - node   - Node to add to the dictionary.
            - parent - The node's parent if it exists.
            - level  - The level in the tree that the node is on.
        """
        nodeChildren = [i for i in self.tree.neighbors(node) if i not in self.tDict]
        self.tDict[node] = nodeInfo(level, parent, nodeChildren)

        for child in nodeChildren:
            self.createTreeDict(child, parent = node, level = level + 1)


    def createLevelsDict(self):
        """
         - Converts a treeDict (as in function above) to a dictionary where
         - each key is the level and the value is the list of nodes on that level.
        """
        for node in self.tDict:
            if self.tDict[node].level not in self.lDict:
                self.lDict[self.tDict[node].level] = []

            self.lDict[self.tDict[node].level].append(node)


class nodeInfo:
    """
     - Stores the following information about a node in the tree:
        - Level    - The level of the tree the node is on.
        - Parent   - The parent of the node, None if the node is the root.
        - Children - A list of the node's children.
    """
    def __init__(self, level, parent, children):
        self.level    = level
        self.parent   = parent
        self.children = children


    def __str__(self):
        return "Level: " + str(self.level) + "\nParent: " + str(self.parent) + "\nChildren: " + str(self.children)
