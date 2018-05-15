#TAGS tree, diameter

# Recursively the tree and returns two pieces of information
# diameter, height

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def diam(tree):
    if tree is None:
        return -1, -1
    dia1, height1 = diam(tree.left)
    dia2, height2 = diam(tree.right)
    height = 1 + max(height1, height2)
    dia = max(dia1, dia2, 2 + height1 + height2)
    return dia, height


class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return diam(root)[0]
