# TAGS TODO

from collections import Counter


def walk(root, seen, sol):
    if root is None:
        return "None"
    else:
        res = (
            "("
            + str(root.val)
            + ","
            + walk(root.left, seen, sol)
            + ","
            + walk(root.right, seen, sol)
            + ")"
        )
        seen[res] += 1
        if seen[res] == 2:
            sol.append(root)
        return res


class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        sol = []
        walk(root, Counter(), sol)
        return list(sol)
