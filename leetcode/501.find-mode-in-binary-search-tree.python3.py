# TAGS bst
from collections import Counter


class Solution:
    def __init__(self):
        self.frequencies = Counter()

    def findMode(self, root):
        if not root:
            return []

        def walk_tree(tree):
            if tree is None:
                return
            walk_tree(tree.left)
            self.frequencies[tree.val] += 1
            walk_tree(tree.right)

        walk_tree(root)
        m = max(self.frequencies.values())
        return [k for (k, v) in self.frequencies.items() if v == m]
