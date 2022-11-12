from ._utils import located
from ._lemma2 import lemma2
from ._lemma3 import lemma3


def case1(self, p, w, d1, k):
    """
     - Case 1: d = 2 and therefore the target set 
     - contains w (vk-1) and  children(vk) excluding vk+1.
     - Args:
        - vk - The leftmost child of w.
        - d  - The distance between the previous probe and the target.
    """
    self["trace"] += "Case 1 called for probe " + str(p) + " and d = " + str(d1) + "\n"

    if self["dkPlus"] == []: #If vk has no children, target located at its parent
        return located(self, self["dkMinus"][0])

    elif len(self.tDict[w].children) == 1: #If vk is the unique child of w then lemma 3
        lemma3(self, w, self.tDict[p].parent, self["dkPlus"][0], self["dkPlus"][-1])
        return

    #Otherwise w has more than one child, zk is its rightmost child
    vkMinus2 = self.tDict[w].parent  #vk-2 is w's parent
    vk = self.tDict[w].children[0]   #vk is w's leftmost child
    yk = self.tDict[w].children[1]   #yk is the child to the right of vk
    zk = self.tDict[w].children[-1]  #zk is w's rightmost child
    s  = self.tDict[w].children[-2]  #s is the child to the left of zk

    if len(self.tDict[zk].children) > 1: #zk has > 1 child, then w.parent has <= 1 child, probe zk
        self["trace"] += "zk has more than one child\n"
        d2 = self.probe(zk)

        if d2 == -1:
            return

        elif d2 == 0:
            return located(self, zk)

        elif d2 == 1:   #If d2 is 1 then the target is at w
            return located(self, w)

        elif d2 == 2: #Target set is w's parent and w's children (minus zk)
            if vkMinus2 is None:  #If w is the root it has no parent, lemma 2 on w's children
                lemma2(self, w, vk, s)
                return

            lemma3(self, vkMinus2, w,  vk,  s)
            return

        elif d2 == 3:   #If d2 is 3 then target is in children(vk) excluding vk + 1, so lemma 2
            lemma2(self, vk, self["dkPlus"][0], self["dkPlus"][-1])
            return

        elif d2 == 4:   #If d2 is 4 then the target is in children(wk+1, xk+1)
            self.lemma4(self["dkPlus"][0], self["dkPlus"][-1], self.tDict[self["dkPlus"][0]].level + 1)
            return

    #Now if zk has at most one child, then we probe w's parent
    elif len(self.tDict[zk].children) <= 1:
        self["trace"] += "zk has at most one child\n"
        d2 = self.probe(vkMinus2)

        if d2 == -1:
            return

        elif d2 == 0:
            return located(self, vkMinus2)

        if d2 == 1:   #If d2 is 1 then the target is at w
            return located(self, w)

        elif d2 == 2:   #If d2 == 2 then the target is in siblings(vk, zk) so lemma 2
            lemma2(self, w, vk, zk)
            return

        elif d2 == 3:   #If d2 is 3 then target is in children(vk) excluding vk + 1, so lemma 2
            lemma2(self, vk, self["dkPlus"][0], self["dkPlus"][-1])
            return

        elif d2 == 4:   #If d2 is 4 then the target is in children(wk+1, xk+1)
            self.lemma4(self["dkPlus"][0], self["dkPlus"][-1], self.tDict[self["dkPlus"][0]].level + 1)
            return
