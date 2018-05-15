#TAGS tree, dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Wrong!! second time I made this mistake
#
# class Solution:
#     def rightSideView(self, root):
#         res = []
#         while root is not None:
#             res.append(root.val)
#             root = root.right or root.left
#         return res
class Solution:
    def rightSideView(self, root):

        view = []

        def walk(tree, level):
            if tree is None:
                return
            if len(view) == level:
                view.append(tree.val)
            walk(tree.right, level+1)
            walk(tree.left, level+1)

        walk(root, 0)
        return view
