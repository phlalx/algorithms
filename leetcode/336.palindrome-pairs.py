# TAGS string, palindrome, trie, dp
# TODO redo, messy


class Tree:
    def __init__(self):
        self.children = {}
        self.index = None


# Use iterative rather than recursive
def insert(t, w, index):
    for c in w:
        t = t.children.setdefault(c, Tree())
    assert t.index is None
    t.index = index


def is_palindrome(w, i, j):
    assert i <= j
    for k in range(i, j):
        if w[k] != w[j - k + i - 1]:
            return False
    return True


def find(t, w, index_w, same_len, res):
    i = 0
    n = len(w)
    # UGLY try to get this right on the first try
    for i in range(n + 1):
        if (
            t.index is not None
            and t.index != index_w
            and is_palindrome(w, i, len(w))
            and (same_len or i != len(w))
        ):
            res.append((index_w, t.index) if same_len else (t.index, index_w))
        if i == n:
            break
        c = w[i]
        t = t.children.get(c)
        if t is None:
            break
    return res


class Solution:
    def palindromePairs(self, words):
        prefix = Tree()
        reverse = Tree()
        for i, w in enumerate(words):
            insert(prefix, w, i)
            insert(reverse, w[::-1], i)
        res = []
        for i, w in enumerate(words):
            find(reverse, w, i, True, res)
            find(prefix, w[::-1], i, False, res)
        return res
