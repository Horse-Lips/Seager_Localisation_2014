import networkx as nx


def located(self, v):
    """
     - Prints that the target has been located at v.
     - Args:
        - v - The vertex that the target was located at.
    """
    print("Target located at node: ", v) if self.verbose else None
    self.tLocation = v


def siblings(self, w, z):
    """
     - Returns the list of siblings of w and z
     - defined as all vertices on  the same level
     - between w and z with the same parent.
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

