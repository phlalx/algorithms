# TAGS BST cool

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Solution 1


class Found(Exception):
    def __init__(self, v):
        self.v = v


# Variant of size
def f(t, k):
    if t is None:
        return 0
    c1 = f(t.left, k)
    if c1 + 1 == k:
        raise Found(t.val)
    assert k - c1 - 1 >= 1
    c2 = f(t.right, k - c1 - 1)
    return c1 + c2 + 1


class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        try:
            f(root, k)
            assert False
        except Found as e:
            return e.v


# Solution 2
#
# k-th element = O(log(n)) if we augment the BST data structure
# with the size of the subtree

# pre-compute size, one pass one the tree
def size(t):
    if t is None:
        return 0
    else:
        res = 1 + size(t.left) + size(t.right)
        t.size = res
        return res


def f(t, k):
    #  l = size(t.left)
    l = t.left.size if t.left else 0
    if k < l:
        # l > 0, we are sure that the tree is not None
        return f(t.left, k)
    elif k == l:
        return t.val
    else:
        return f(t.right, k - l - 1)


class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        size(root)
        return f(root, k - 1)
