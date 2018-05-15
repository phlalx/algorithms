# TAGS bst
#
# fast but we don't use the bst property and not constant space
# we could do in constant space using two iterators
# (think 2 sum in constant space)


class TreeNode:
    def __init__(self, x, y=None, z=None):
        self.val = x
        self.left = y
        self.right = z


class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        seen = set()

        def walk(root):
            if root is None:
                return False
            if walk(root.left):
                return True
            if k - root.val in seen:
                return True
            seen.add(root.val)
            return walk(root.right)

        return walk(root)
