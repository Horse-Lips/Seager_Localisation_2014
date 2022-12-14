from ._lemma2 import lemma2
from ._lemma3 import lemma3


def case4(self, p, w, d1, k):
    """
     - Case 4: d = 4, so dk-1 and dk+1 will contain nodes
    """
    self["trace"] += "Case 4 called for probe " + str(p) + " and d = " + str(d1) + "\n"

    if self["dkPlus"]    == []:    #dk+1 empty, target in dkMinus, these are siblings so lemma 2
        lemma2(self, self.tDict[self["dkMinus"][0]].parent, self["dkMinus"][0], self["dkMinus"][-1])
        return

    elif self["dkMinus"] == []:     #dk-1 empty, so target set in dkPlus (children(wk, zk)) so lemma 4
        self.lemma4(self.tDict[self["dkPlus"][0]].parent, self.tDict[self["dkPlus"][-1]].parent, k + 1)
        return

    self["trace"] += "Assigning zk-1 to node " + str(self["dkMinus"][-1]) + "\n"
    zkMinus = self["dkMinus"][-1]   #Get zk, wk-2's rightmost child
    
    p2, minus = (zkMinus, 1) if self.tDict[zkMinus].children == [] else (self.tDict[zkMinus].children[0], 0)

    d2 = self.probe(p2)  #Probe zk's first child or zk if there are no children

    if d2 == 1:
        return self.located(self.tDict[p2].parent)

    elif d2 == 2:
        if minus:
            lemma2(self, self.tDict[zkMinus].parent, self["dkMinus"][0], self["dkMinus"][-2])
            return

        if len(self.tDict[zkMinus].children) == 1:    #zk is zk-1's only child, target at zk's parent
            return self.located(self.tDict[zkMinus].parent)

        d3 = self.probe(w)

        if d3 == 1:
            return self.located(self.tDict[w].parent)

        elif d3 == 2:
            vkMinus2 = self.tDict[w].parent
            vkMinus3 = self.tDict[self.tDict[w].parent].parent

            if vkMinus3 is None:
                lemma2(self, vkMinus2, self["dkMinus"][0], self["dkMinus"][-1])
                return

            lemma3(self, vkMinus3, vkMinus2, self["dkMinus"][0], self["dkMinus"][-1])
            return

        elif d3 == 3:
            lemma2(self, zkMinus, self.tDict[zkMinus].children[0], self.tDict[zkMinus].children[-1])
            return

        elif d3 == 4:
            self.lemma4(self.tDict[zkMinus].children[1], self.tDict[zkMinus].children[-1], self.tDict[zkMinus].level + 2)
            return

    elif d2 == 3:
        if minus:
            #Same as d2 == 4 and no minus
            t = self.siblings(w, zkMinus)[self.siblings(w, zkMinus).index(zkMinus) - 1]

            self.lemma4(w, t, self.tDict[w].level + 1)
            return

        if len(self["dkMinus"]) == 2:   #there's one other vertex on zk.level, it's 3 away so target found
            return self.located(self["dkMinus"][0])

        #Otherwise the target is in the siblings of wk-2's children, so lemma 2
        lemma2(self, self.tDict[zkMinus].parent, self["dkMinus"][0], self["dkMinus"][-2])
        return

    elif d2 == 4:
        if minus:
            #Same as d2 == 5 and no minus
            self.lemma4(self.tDict[w].children[1], self.tDict[w].children[-1], self.tDict[w].level + 2)
            return

        #If d = 4 then the target is in Children(vk-1, t) where t is zk's predecessor, so lemma 4
        t = self.siblings(w, zkMinus)[self.siblings(w, zkMinus).index(zkMinus) - 1]

        self.lemma4(w, t, self.tDict[w].level + 1)
        return

    elif d2 == 5:
        if minus:
            #Same as d2 == 6 and no minus
            wk = self.tDict[w].children[1]
            xk = self.tDict[w].children[-1]

            self.lemma4(self.tDict[wk].children[0], self.tDict[xk].children[-1], self.tDict[wk].level + 2)
            return

        #If d = 5 then the target is in the children of the children of w (apart from vk)
        self.lemma4(self.tDict[w].children[1],self.tDict[w].children[-1],self.tDict[w].level+2)
        return

    elif d2 == 6:
        #Finally if d is 6 then the target is in the children of children of children of w (apart from vk)
        wk = self.tDict[w].children[1]
        xk = self.tDict[w].children[-1]

        self.lemma4(self.tDict[wk].children[0], self.tDict[xk].children[-1], self.tDict[wk].level + 2)
        return

