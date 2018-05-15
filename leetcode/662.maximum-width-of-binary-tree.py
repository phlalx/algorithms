# TAGS tree
# see 637

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Trick compute node "rank" for each element of the tree, and keep
# max/min rank at each level

class Solution:
    def widthOfBinaryTree(self, root):
        left = {}
        right = {}

        def walk(tree, level, pos):
            if tree is None:
                return
            if level not in left:
                left[level] = pos
            if level not in right or right[level] < pos:
                right[level] = pos
            walk(tree.left, level+1, 2 * pos)
            walk(tree.right, level+1, 2 * pos + 1)

        walk(root, 0, 0)
        n = min(max(left.keys()), max(right.keys()))
        return max(right[i] - left[i] + 1 for i in range(n+1))
