from ._utils import located
from ._lemma2 import lemma2


def case2(self, p, w, d, k):
    """
     - Case 2: d is 2 or 3, so the target set is the children of w minus vk.
     - Args:
        - w  - The leftmost sibling in siblings(w, z) in lemma 4.
        - vk - The leftmost child of w.
    """
    self["trace"] += "Case 2 called for probe " + str(p) + " and d = ", str(d) + "\n"

    if len(self["dk"]) == 1:
        return located(self, self["dk"][0])

    lemma2(self, w, self["dk"][0], self["dk"][-1])
    return

