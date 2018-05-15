# TAGS bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# herite
def is_valid_2(t, a, b):
    if t is None:
        return True
    res = (
        a < t.val < b and is_valid_2(t.left, a, t.val) and is_valid_2(t.right, t.val, b)
    )
    return res

def isValidBST(self, root: TreeNode) -> bool:
    def f(node) -> Tuple[bool, int, int]:  # is_bst, mi, max
        if not node:
            return True, float('inf'), float('-inf')
        lbst, lmi, lma = f(node.left)
        rbst, rmi, rma = f(node.right)
        bst = lbst and rbst and lma < node.val < rmi
        mi = min(lmi, rmi, node.val)
        ma = max(lma, rma, node.val)
        return bst, mi, ma
    return f(root)[0]

# More symmetric, but more redondancy
#
# def is_valid(t):
#     if t.left is None and t.right is None:
#         return True, t.val, t.val
#     elif t.left is None:
#         rval, rmin, rmax = is_valid(t.right)
#         return rval and rmin >= t.val, t.val, rmax
#     elif t.right is None:
#         lval, lmin, lmax = is_valid(t.left)
#         return lval and t.val >= lmax, lmin, t.val
#     else:
#         rval, rmin, rmax = is_valid(t.right)
#         lval, lmin, lmax = is_valid(t.left)
#         return lval and rval and lmax <= t.val <= rmin, lmin, rmax

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        # return is_valid(root)[0]
        return is_valid_2(root, float("-inf"), float("inf"))
