from networkx import shortest_path_length, single_source_dijkstra_path_length
from random   import choice
from ._lemma1 import lemma1
from ._lemma2 import lemma2
from ._case1  import case1
from ._case2  import case2
from ._case3  import case3
from ._case4  import case4
from ._case5  import case5


class nodeInfo:
    """
     - Stores information about nodes in a tree.
     - Variables:
        - Level    - Level of node in the tree.
        - Parent   - Parent of node, None if root.
        - Children - List of the node's children.
    """
    def __init__(self, level, parent, children):
        self.level    = level
        self.parent   = parent
        self.children = children


class Seager:
    """
     - Class for the Seager 2014 localisation strategy for trees.
     - The solve() method is the main function after initialisation.
     - Variables:
        - tree  - NetworkX tree object rooted at node 0
        - tDict - Dict representation of the tree (See createTreeDict function)
        - lDict - Dict of lists of nodes at each tree level (see createLevelsDict function)
        - iDict - Dict of relevant information during execution containing:
            - trace                 - Verbose information about the execution
            - k                     - The level marked as k at current stage of execution
            - dkMinus, dk, dkPlus   - Target locations on levels k - 1, k, k + 1
            - probeNum, probeList   - Current probe number and list of all previously probed vertices
            - t, tLocation          - List of target locations, final target location. t can be preset as node list
            - l, vl, yl, zl         - Level l in the tree and associated nodes (case 5)
    """
    def __init__(self, tree):
        self.tree  = tree   #NetworkX tree object (Rooted at node 0)
        self.tDict = dict() #Dict representation of tree object (See createTreeDict)  
        self.lDict = dict() #Dict of level information of the tree object (See createLevelsDict)
        self.iDict = dict() #Dict containing relevant information during execution

        self.createTreeDict(0)  #Initialise the tree dict
        self.createLevelsDict() #Initialise the levels dict

        self["trace"] = ""  #Trace of execution for verbose output


    def __setitem__(self, key, value):
        self.iDict[key] = value


    def __getitem__(self, key):
        try:    return self.iDict[key]
        except: return None


    def solve(self):
        """
         - Carries out the strategy of theorem 8.
        """
        d = self.probe(0)   #Probe root

        if lemma1(self) != -1 and d != -1:  #Organise tree and check for hideouts
            if len(self.lDict[d]) == 1:
                return self.located(self.lDict[d][0])

            self.lemma4(self.tDict[self.lDict[d][0]].parent, self.tDict[self.lDict[d][-1]].parent, d)


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
        self["trace"] += "Lemma 4 called for Children(" + str(w) + ", " + str(z) + ") on level " + str(k) + "\n"

        if w == z and self.tDict[w].children == []: return self.located(w)

        w, z      = self.reduceSet(w, z)   #Replace w with w', z with z' if no children
        self["k"] = k                       #Set global value of level k
        self.setDSets(w, z)                 #Set dk to Children(w, z) and expand

        if len(self["dk"]) == 1:                    return self.located(self["dk"][0])
        
        vk     = self["dk"][0]  #Let vk be the first child of w
        self["trace"] += "Assigned vk to node: " + str(vk) + "\n"
            

        p, d = (vk, 1) if len(self.tDict[vk].children) == 0 else (self["dkPlus"][0], 0)
        d1   = self.probe(p)
        ds   = self.updateDSets(p, d1)

        if ds != -1:
            self["trace"] += "located by dist set update\n"
            return

        elif d1 == 1:
            return self.located(self.tDict[p].parent)

        elif d1 == 2:
            if d:   #If probed vk and d1 == 2 then lemma 2 w's other children
                lemma2(self, w, self["dk"][0], self["dk"][-1])

            elif w == z and len(self.tDict[vk].children) == 1:
                return self.located(w)

            else:
                case1(self, p, w, d1, k)

        elif d1 == 3:
            if d:   #If probed vk and d1 == 3 then case 4 (dk-1 and dk+1 non-empty)
                case4(self, p, w, d1, k)

            else:
                case2(self, p, w, d1, k)

        elif d1 == 4:
            if d:   #If probed vk and d1 == 4 then target in subset of Children(w, z)
                self.lemma4(self.tDict[self["dk"][0]].parent, self.tDict[self["dk"][-1]].parent, k)

            else:
                case4(self, p, w, d1, k)

        elif d1 % 2 == 1 and d1 > 3:
            if d:   #If vk probed then dk+1 and dk-1 possible
                if self["dkMinus"] == [] and self["dkPlus"] != []:
                    self.lemma4(self.tDict[self["dkPlus"][0]].parent, self.tDict[self["dkPlus"][-1]].parent, self["k"] + 1)

                elif self["dkPlus"] == [] and self["dkMinus"] != []:
                    self.lemma4(self.tDict[self["dkMinus"][0]].parent, self.tDict[self["dkMinus"][-1]].parent, self["k"] - 1)

                elif self["dkMinus"] == [] and self["dkPlus"] == []:
                    print("====== Lemma 4 line 138 - dkPlus and dkMinus both empty ======")
                    print(self["dkMinus"])
                    print(self["dk"])
                    print(self["dkPlus"])

                else:
                    case5(self, p, w, d1, self["dkMinus"][-1])

            else:
                case3(self, p, w, d1, k)

        elif d1 % 2 == 0 and d1 > 5:
            if d:
                self.lemma4(self.tDict[self["dkMinus"][0]].parent, self.tDict[self["dk"][-1]].parent, k)

            elif self["dkMinus"] == []:
                self.lemma4(self.tDict[self["dkPlus"][0]].parent, self.tDict[self["dkPlus"][-1]].parent, k + 1)

            elif self["dkPlus"] == []:
                self.lemma4(self.tDict[self["dkMinus"][0]].parent, self.tDict[self["dkMinus"][-1]].parent, k - 1)

            else:
                case5(self, p, w, d1, self["dkMinus"][-1])


    def probe(self, v):
        """
         - Returns the distance from v to the target
        """
        if self["probeNum"] is None:
            self["probeNum"]  = 0
            self["probeList"] = []

        if self["t"] is None:
            self["t"] = [choice(range(len(self.tree)))]

        self["probeList"].append(v)

        if self["probeNum"] == len(self["t"]):    #Move target randomly if the target move set is empty
            self["t"].append(choice([i for i in self.tree.neighbors(self["t"][-1])]))

        self["probeNum"] += 1

        d  = shortest_path_length(self.tree, v, self["t"][self["probeNum"] - 1])

        self["trace"] += "Probing node: " + str(v) + " for target at node " + str(self["t"][self["probeNum"] - 1])
        self["trace"] += " and d = " + str(d) + "\n"

        if d == 0:
            self.located(v)
            return -1

        return d

        
    def updateDSets(self, v, d):
        """
         - Updates the sets Dk-1, Dk, Dk+1
        """
        distances = single_source_dijkstra_path_length(self.tree, v)
        dkMinus, dk, dkPlus = [], [], []

        tSet = self["dkMinus"] + self["dk"] + self["dkPlus"]

        for i in distances:
            if distances[i] == d and i in tSet:
                if self.tDict[i].level == self["k"] - 1:
                    dkMinus.append(i)

                elif self.tDict[i].level == self["k"]:
                    dk.append(i)

                elif self.tDict[i].level == self["k"] + 1:
                    dkPlus.append(i)

        tSetNew = dkMinus + dk + dkPlus

        if len(tSetNew) == 1:
            return self.located(tSetNew[0])

        self["dkMinus"], self["dk"], self["dkPlus"] = dkMinus, dk, dkPlus
        return -1


    def setDSets(self, w, z):
        """
         - Expands Dk-1, Dk, and Dk+1 simulating target movement
        """
        self["dkMinus"] = []
        self["dk"]      = self.children(w, z)  #Set dk sets
        self["dkPlus"]  = []

        for n in self["dk"]:
            if self.tDict[n].parent not in self["dkMinus"]:
                self["dkMinus"].append(self.tDict[n].parent)

            for c in self.tDict[n].children:
                if c not in self["dkPlus"]:
                    self["dkPlus"].append(c)


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


    def located(self, v):
        """
         - Sets the target as located at node v.
         - Args:
            - v - The vertex that the target was located at.
        """
        self["trace"] += "Target located at node: " + str(v) + "\n"
        self["tLocation"] = v


    def siblings(self, w, z):
        """
         - Returns list of siblings(w, z) defined as all vertices
         - on the same level between w and z with the same parent.
         - Args:
            - w - The leftmost sibling in the set.
            - z - The rightmost sibling in the set.

         - Returns:
            -   - The set of Siblings(w, z) as defined above.
        """
        if self.tDict[w].parent != self.tDict[z].parent:
            return

        allChildren = self.tDict[self.tDict[w].parent].children

        return allChildren[allChildren.index(w):allChildren.index(z) + 1]


    def children(self, w, z):
        """
         - Returns the list of children of vertices between
         - and including w and z on the same level.
         - Args:
            - w - The leftmost vertex of the subset of the level.
            - z - The rightmost vertex of the subset of the level.

         - Returns:
            -   - The set of Children(w, z) as defined above.
        """
        levelK    = self.lDict[self.tDict[w].level]
        childList = []

        for node in levelK[levelK.index(w):levelK.index(z) + 1]:
            for child in self.tDict[node].children:
                childList.append(child)

        return childList


    def reduceSet(self, w, z):
        """
         - Replaces w with w' and z with z' if they have
         - no children. Used at the start of Lemma 4.
        """
        levelK = self.lDict[self.tDict[w].level]
        wIndex, zIndex = levelK.index(w), levelK.index(z)

        while self.tDict[levelK[wIndex]].children == []:
            wIndex += 1

        while self.tDict[levelK[zIndex]].children == []:
            zIndex -= 1

        return levelK[wIndex], levelK[zIndex]

