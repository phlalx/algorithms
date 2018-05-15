# TAGS tree


class TreeNode:
    def __init__(self, x, y=None, z=None):
        self.val = x
        self.left = y
        self.right = z


def listToTree(x):
    return x


def equalTree(t1, t2):
    if t1 and t2:
        if t1.val != t2.val:
            return False
        else:
            return equalTree(t1.left, t2.left) and equalTree(t1.right, t2.right)
    else:
        return (not t1) and (not t2)


class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s:
            return (
                equalTree(s, t)
                or self.isSubtree(s.left, t)
                or self.isSubtree(s.right, t)
            )
        else:
            return not t
