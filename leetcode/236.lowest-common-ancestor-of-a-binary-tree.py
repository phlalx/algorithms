# TAGS tree traversal
# TRICK careful that p and q are TreeNodes and not int

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def f(root, p, q):
    if root is None:
        return False, False, None
    p1, q1, lca1 = f(root.left, p, q)
    p2, q2, lca2 = f(root.right, p, q)
    v = root.val

    if v == p:
        if q1 or q2:
            return True, True, root
        else:
            return True, False, None
    if v == q:
        if p1 or p2:
            return True, True, root
        else:
            return False, True, None
    if lca1:
        assert p1 and q1
        return True, True, lca1
    if lca2:
        assert p2 and q2
        return True, True, lca2
    if (p1 and q2) or (p2 and q1):
        return True, True, root
    return p1 or p2, q1 or q2, None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p == q:
            return p
        return f(root, p.val, q.val)[2]
