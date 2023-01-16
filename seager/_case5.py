from ._lemma2 import lemma2


def lVariables(self, d, p):
    self["l"] = self["k"] - (d // 2)    #Get level l in the tree (highest level path to target can reach)

    self["vl"] = p              #Get vl
    while self.tDict[self["vl"]].level != self["l"]:
        self["vl"] = self.tDict[self["vl"]].parent

    self["yl"] = p              #Get yl
    while self.tDict[self["yl"]].level != self["l"]:
        self["yl"] = self.tDict[self["yl"]].parent

    self["zl"] = p              #Get zl
    while self.tDict[self["zl"]].level != self["l"]:
        self["zl"] = self.tDict[self["zl"]].parent


def case5(self, p, w, d1, zkMinus):
    self["trace"] += "Case 5 called for probe " + str(p) + " and d = " + str(d1) + "\n"

    lVariables(self, d1, p)

    zkMinus2 = self.tDict[zkMinus].parent

    if zkMinus == self.tDict[zkMinus2].children[-1]:
        d2 = self.probe(self["vl"])
        
        if d2 == -1:
            return

        else:
            case5a(self, p, w, d1, d2)
            return

    elif zkMinus == self.tDict[zkMinus2].children[0] and len(self.tDict[zkMinus2].children) > 1 and len(self.tDict[zkMinus].children) > 1:
        case5b(self, p, w, d1)
        return

    elif zkMinus != self.tDict[zkMinus2].children[-1] and len(self.tDict[zkMinus].children) < 2:
        case5c(self, p, w, d1)
        return


def case5a(self, p, w, d1, d2):
    self["trace"] += "Case 5a called for probe " + str(p) + " and d1 = " + str(d1) + " and d2 = " + str(d2) + "\n"

    wkPlus,  xkPlus  = self["dkPlus"][0],  self["dkPlus"][-1]
    ykMinus, zkMinus = self["dkMinus"][0], self["dkMinus"][-1]

    if d2 == -1:
        return

    elif d2 == (d1 // 2) + 2:
        self.lemma4(wkPlus, xkPlus, self.tDict[wkPlus].level + 1)
        return

    elif d2 == (d1 // 2) + 1:
        self.lemma4(self.tDict[wkPlus].parent, self.tDict[xkPlus].parent, self.tDict[wkPlus].level)
        return

    elif d2 == (d1 // 2) - 1:
        self.lemma4(self.tDict[ykMinus].parent, self.tDict[zkMinus].parent, self.tDict[ykMinus].level)
        return

    elif d2 == (d1 // 2) - 2:
        ykMinus2, zkMinus2 = self.tDict[ykMinus].parent,  self.tDict[zkMinus].parent

        if d1 != 6:
            ykMinus3, zkMinus3 = self.tDict[ykMinus2].parent, self.tDict[zkMinus2].parent

            self.lemma4(ykMinus3, zkMinus3, self.tDict[zkMinus2].level)
            return

        elif d1 == 6:
            lemma2(self, self.tDict[ykMinus2].parent, ykMinus2, zkMinus2)
            return

    elif d2 == d1 // 2:
        self.lemma4(self.tDict[self.tDict[wkPlus].parent].parent, self.tDict[self.tDict[xkPlus].parent].parent, self.tDict[self.tDict[wkPlus].parent].level)
        return

    elif d2 == d1:
        print("dkMinus:", self["dkMinus"])
        print("dk:", self["dk"])
        print("dkPlus:", self["dkPlus"])

    print("End of Func. d2:", d2, "d1:", d1)


def case5b(self, p, w, d1):
    self["trace"] += "Case 5b called for probe " + str(p) + " and d = " + str(d1) + "\n"

    wk = self.tDict[self["dkPlus"][0]].parent
    xk = self.tDict[self["dkPlus"][-1]].parent

    zkMinus  = self["dkMinus"][-1]
    zkMinus2 = self.tDict[zkMinus].parent

    zlPlus = self["dkMinus"][-1]

    while self.tDict[zlPlus].level != self["l"]+ 1:
        zlPlus = self.tDict[zlPlus].parent

    self["trace"] += "Probing zk-2 at node: " + str(zkMinus2) + "\n"

    d2 = self.probe(zkMinus2)

    if d2 == 1:
        return self.located(zkMinus)

    elif d2 == d1:
        self.lemma4(self["dkPlus"][0], self["dkPlus"][-1], self.tDict[self["dkPlus"][0]].level + 1)
        return

    elif d2 == d1 - 1:
        self.lemma4(wk, xk, self.tDict[wk].level + 1)
        return

    elif d2 == d1 - 2:
        kMinus   = self.lDict[self["k"] - 1]

        for i in range(len(kMinus) - 1, 0, -1):
            r = kMinus[i]

            while r != zlPlus and r != self["zl"]:
                r = self.tDict[r].parent

            if r == self["zl"]:
                t = kMinus[i]
                break

        self.lemma4(self.tDict[wk].parent, t, self.tDict[wk].level + 1)
        return

    case5bExtraCase(self, zkMinus2, w, d1, d2)


def case5bExtraCase(self, p, w, d1, d2):
    self["trace"] += "Case 5b extra case called for d1 = " + str(d1) + " and d2 = " + str(d2) + "\n"

    #d2 is odd with 3 <= d2 <= d1 - 3 or similarly for case 5c
    if d2 % 2 != 0 and (3 <= d2 <= d1 - 3 or 5 <= d2 <= d1 + 2):
        m = (d2 - 1) / 2
        levelPlus = self["k"] - m - 1

        stPlus = self["dkMinus"][-1]
        while self.tDict[stPlus].level != levelPlus:
            stPlus = self.tDict[stPlus].parent

        stRoot = self.tDict[stPlus].parent

        kMinus   = self.lDict[self["k"] - 1]

        for i in range(len(kMinus) - 1, 0, -1):
            r = kMinus[i]

            while r != stPlus and r != stRoot:
                r = self.tDict[r].parent

            if r == stRoot:
                t = kMinus[i]
                break

        for i in range(0, len(kMinus)):
            r = kMinus[i]

            while r != stPlus and r != stRoot:
                r = self.tDict[r].parent

            if r == stRoot:
                s = kMinus[i]
                break

        self.lemma4(s, t, self.tDict[s].level + 1)
        return

    elif d2 % 2 == 0 and (4 <= d2 <= d1 - 4 or 6 <= d2 <= d1 + 2):
        m = d2 / 2
        levelPlus = self["k"] - m

        q, R, s, t = None, None, None, None

        qrPlus = self["dkMinus"][-1]
        while qrPlus is not None and self.tDict[qrPlus].level != levelPlus:
            qrPlus = self.tDict[qrPlus].parent

        if qrPlus is not None:
            qrRoot = self.tDict[qrPlus].parent

            levelK   = self.lDict[self["k"]]

            for i in range(len(levelK) - 1, 0, -1):
                r = levelK[i]

                while r != qrPlus and r != qrRoot and r != None:
                    r = self.tDict[r].parent

                if r == qrRoot:
                    R = levelK[i]
                    break

            for i in range(0, len(levelK)):
                r = levelK[i]

                while r != qrPlus and r != qrRoot and r != None:
                    r = self.tDict[r].parent

                if r == qrRoot:
                    q = levelK[i]
                    break


        levelPlus = self["k"] - m - 1

        stPlus = self["dkMinus"][-1]
        while stPlus is not None and self.tDict[stPlus].level != levelPlus:
            stPlus = self.tDict[stPlus].parent

        if stPlus is not None:
            stRoot = self.tDict[stPlus].parent

            kMinusMinus   = self.lDict[self["k"] - 2]

            for i in range(len(kMinusMinus) - 1, 0, -1):
                r = kMinusMinus[i]

                while r != stPlus and r != stRoot and r != None:
                    r = self.tDict[r].parent

                if r == stRoot:
                    t = kMinusMinus[i]
                    break

            for i in range(0, len(kMinusMinus)):
                r = kMinusMinus[i]

                while r != stPlus and r != stRoot and r != None:
                    r = self.tDict[r].parent

                if r == stRoot:
                    s = kMinusMinus[i]
                    break

        q = self.tDict[q].parent if q is not None else None
        R = self.tDict[R].parent if R is not None else None

        s = self.tDict[s].parent if s is not None else None
        t = self.tDict[t].parent if t is not None else None

        if q == None and R == None and s == None and t == None:
            print("====== ALL OF S, T, Q, R, ARE NONE ======")
            print(self["trace"])
            return


        if q == None or R == None or self.children(q, R) == []:
            self.lemma4(s, t, self.tDict[s].level + 1)
            return

        elif s == None or t == None or self.children(s, t) == []:
            self.lemma4(q, R, self.tDict[q].level + 1)
            return

        lVariables(self, d2, p)
        d3 = self.probe(self["vl"])

        self["dkMinus"] = self.children(self.tDict[s].parent, self.tDict[t].parent)
        self["dk"]      = []
        self["dkPlus"]  = self.children(self.tDict[q].parent, self.tDict[R].parent)

        self["k"] = self.tDict[s].level + 1

        case5a(self, p, w, d2, d3)
        return


def case5c(self, p, w, d1):
    self["trace"] += "Case 5c called for probe " + str(p) + " and d = " + str(d1) + "\n"

    zkMinus2 = self.tDict[self["dkMinus"][-1]].parent
    zkMinus  = self["dkMinus"][-1]
    zk       = self.tDict[zkMinus].children[0]
    zkMinusPred   = self["dkMinus"][self["dkMinus"].index(zkMinus) - 1]

    d2 = self.probe(zk)

    if d2 == 1:
        return self.located(self["dkMinus"][-1])

    elif d2 == 2:
        return self.located(self.tDict[self["dkMinus"][-1]].parent)

    elif d2 == 3:
        t = self.tDict[zkMinus2].children[0]

        lemma2(self, zkMinus2, t, zkMinusPred)
        return

    elif d2 == 4:
        zkMinus3 = self.tDict[zkMinus2].parent
        d3 = self.probe(zkMinus3)

        if d3 == 1:
            zkMinus3Children = self.tDict[zkMinus3].children
            s = zkMinus3Children[0]
            zkMinus2Pred = zkMinus3Children[zkMinus3Children.index(zkMinus2) - 1]

            lemma2(self, zkMinus3, s, zkMinus2Pred)
            return

        elif d3 == 2:
            case5(self, p, w, d1, zkMinusPred)
            return

        elif d3 == 3:
            self.lemma4(t, zkMinusPred, self.tDict[t].level + 1)
            return

        elif d3 == 4:
            q = self.tDict[t].children[0]
            r = self.tDict[zkMinusPred][-1]

            self.lemma4(q, r, self.tDict[r].level + 1)
            return

    elif 5 <= d2 <= d1 + 2:
        case5bExtraCase(self, p, w, d1, d2)
        return

