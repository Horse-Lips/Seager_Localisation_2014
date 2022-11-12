from ._utils import located
from ._lemma2 import lemma2
from ._utils import children


def case5(self, p, w, d1, zkMinus):
    print("Case 5 called for probe", p, "d =", d1) if self.verbose else None

    self.l = self.k - (d1 // 2)    #Get level l in the tree (highest level path to target can reach)

    self.vl = p              #Get vl
    while self.tDict[self.vl].level != self.l:
        self.vl = self.tDict[self.vl].parent

    self.yl = p              #Get yl
    while self.tDict[self.yl].level != self.l:
        self.yl = self.tDict[self.yl].parent

    self.zl = p              #Get zl
    while self.tDict[self.zl].level != self.l:
        self.zl = self.tDict[self.zl].parent


    if zkMinus == self.tDict[self.tDict[zkMinus].parent].children[-1]:
        d2 = self.probe(self.vl)
        
        if d2 == -1:
            return

        else:
            case5a(self, p, w, d1, d2)
            return

    elif zkMinus == self.tDict[self.tDict[zkMinus].parent].children[0] and len(self.tDict[self.tDict[self.dkMinus[-1]].parent].children) > 1:
        case5b(self, p, w, d1)
        return

    elif zkMinus != self.tDict[self.tDict[zkMinus].parent].children[-1] and len(self.tDict[self.dkMinus[-1]].children) <= 1:
        case5c(self, p, w, d1)
        return


def case5a(self, p, w, d1, d2):
    print("Case 5a called for probe", p, "d1 =", d1, "d2 =", d2) if self.verbose else None

    if d2 == -1:
        return

    elif d2 == (d1 // 2) + 2:
        self.lemma4(self.dkPlus[0], self.dkPlus[-1], self.k + 2)
        return

    elif d2 == (d1 // 2) + 1:
        self.lemma4(self.tDict[self.dkPlus[0]].parent, self.tDict[self.dkPlus[-1]].parent, self.k + 1)
        return

    elif d2 == (d1 // 2) - 1:
        self.lemma4(self.tDict[self.dkMinus[0]].parent, self.tDict[self.dkMinus[-1]].parent, self.k - 1)
        return

    elif d2 == (d1 // 2) - 2:
        if d1 != 6:
            self.lemma4(self.tDict[self.tDict[self.dkMinus[0]].parent].parent, self.tDict[self.tDict[self.dkMinus[-1]].parent].parent, self.k - 2)
            return

        elif d1 == 6:
            lemma2(self, self.tDict[self.tDict[self.dkMinus[0]].parent].parent, self.tDict[self.dkMinus[0]].parent, self.tDict[self.dkMinus[-1]].parent)
            return

    elif d2 == d1 // 2:
        self.lemma4(self.tDict[self.tDict[self.dkPlus[0]].parent].parent, self.dkMinus[-1], self.k)
        return


def case5b(self, p, w, d1):
    print("Case 5b called for probe", p, "d =", d1) if self.verbose else None

    wk = self.tDict[self.dkPlus[0]].parent
    xk = self.tDict[self.dkPlus[-1]].parent

    zkMinus2 = self.tDict[self.dkMinus[-1]].parent
    zkMinus  = self.dkMinus[-1]

    zlPlus = self.dkMinus[-1]

    while self.tDict[zlPlus].level != self.l + 1:
        zlPlus = self.tDict[zlPlus].parent

    if self.verbose:
        print("Probing zk-2 at node:", zkMinus2)

    d2 = self.probe(zkMinus2)

    if d2 == -1:
        return

    elif d2 == 0:
        return located(self, zkMinus2)

    elif d2 == 1:
        return located(self, zkMinus)

    elif d2 == 2:
        self.lemma4(self.tDict[zkMinus].children[0], self.tDict[zkMinus].children[-1], self.k + 1)
        return

    elif d2 == d1:
        self.lemma4(self.dkPlus[0], self.dkPlus[-1], self.k + 2)
        return

    elif d2 == d1 - 1:
        self.lemma4(wk, xk, self.k + 1)
        return

    elif d2 == d1 - 2:
        kMinus   = self.lDict[self.k - 1]

        for i in range(len(kMinus) - 1, 0, -1):
            r = kMinus[i]

            while r != zlPlus and r != self.zl:
                r = self.tDict[r].parent

            if r == self.zl:
                t = kMinus[i]
                break

        self.lemma4(self.tDict[wk].parent, t, self.k)
        return

    else:
        case5bExtraCase(self, zkMinus2, w, d1, d2)


def case5bExtraCase(self, p, w, d1, d2):
    print("Case 5b extra case called for d1 =", d1, "d2 =", d2) if self.verbose else None

    #d2 is odd with 3 <= d2 <= d1 - 3 or similarly for case 5c
    if d2 % 2 != 0 and (3 <= d2 <= d1 - 3 or 5 <= d2 <= d1 - 5):
        m = (d2 - 1) / 2
        levelPlus = self.k - m - 1

        stPlus = self.dkMinus[-1]
        while self.tDict[stPlus].level != levelPlus:
            stPlus = self.tDict[stPlus].parent

        stRoot = self.tDict[stPlus].parent

        kMinus   = self.lDict[self.k - 1]

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

        self.lemma4(s, t, k)
        return

    elif d2 % 2 == 0 and (4 <= d2 <= d1 - 4 or 6 <= d2 <= d1 - 6):
        m = d2 / 2
        levelPlus = self.k - m

        q, R, s, t = None, None, None, None

        qrPlus = self.dkMinus[-1]
        while self.tDict[qrPlus].level != levelPlus:
            qrPlus = self.tDict[qrPlus].parent

        qrRoot = self.tDict[qrPlus].parent

        levelK   = self.lDict[self.k]

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


        levelPlus = self.k - m - 1

        stPlus = self.dkMinus[-1]
        while self.tDict[stPlus].level != levelPlus:
            stPlus = self.tDict[stPlus].parent

        stRoot = self.tDict[stPlus].parent

        kMinusMinus   = self.lDict[self.k - 2]

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
        print("(q, r) =", q, R)

        s = self.tDict[s].parent if s is not None else None
        t = self.tDict[t].parent if t is not None else None
        print("(s, t) =", s, t)

        if q == None or R == None or children(self, q, R) == []:
            self.lemma4(s, t, self.tDict[s].level + 1)
            return

        elif s == None or t == None or children(self, s, t) == []:
            self.lemma4(q, R, self.tDict[q].level + 1)
            return

        d3 = self.probe(self.vl)

        if d3 == -1:
            return

        else:
            self.dkMinus = children(self, self.tDict[s].parent, self.tDict[t].parent)
            self.dk      = []
            self.dkPlus  = children(self, self.tDict[q].parent, self.tDict[R].parent)

            self.k = self.tDict[s].level + 1

            case5a(self, p, w, d2, d3)
            return


def case5c(self, p, w, d1):
    print("Case 5c called for probe", p, "d =", d1) if self.verbose else None

    zkMinus2 = self.tDict[self.dkMinus[-1]].parent
    zkMinus  = self.dkMinus[-1]
    zk       = self.tDict[zkMinus].children[0]
    zkMinusPred   = self.dkMinus[self.dkMinus.index(zkMinus) - 1]

    d2 = self.probe(zk)

    if d2 == -1:
        return

    elif d2 == 0:
        return located(self, zk)

    elif d2 == 1:
        return located(self, self.dkMinus[-1])

    elif d2 == 2:
        return located(self, self.tDict[self.dkMinus[-1]].parent)

    elif d2 == 3:
        t = self.tDict[zkMinus2].children[0]

        lemma2(self, zkMinus2, t, zkMinusPred)
        return

    elif d2 == 4:
        zkMinus3 = self.tDict[zkMinus2].parent
        d3 = self.probe(zkMinus3)

        if d3 == -1:
            return

        elif d3 == 0:
            return located(self, zkMinus3)

        elif d3 == 1:
            zkMinus3Children = self.tDict[zkMinus3].children
            s = zkMinus3Children[0]
            zkMinus2Pred = zkMinus3Children[zkMinus3Children.index(zkMinus2) - 1]

            lemma2(self, zkMinus3, s, zkMinus2Pred)
            return

        elif d3 == 2:
            case5(self, p, w, d1, zkMinusPred) if self.verbose else None
            return

        elif d3 == 3:
            self.lemma4(t, zkMinusPred, k)
            return

        elif d3 == 4:
            q = self.tDict[t].children[0]
            r = self.tDict[zkMinusPred][-1]

            self.lemma4(q, r, self.tDict[r].level + 1)
            return

    elif 5 <= d2 <= d1 + 2:
        case5bExtraCase(self, p, w, d1, d2)
        return

