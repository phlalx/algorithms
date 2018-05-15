# TAGS binary tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def f(root, path, all_paths):
    path.append(root.val)
    if not root.left and not root.right:  # leaf
        repr = "->".join(map(str, path))
        all_paths.append(repr)
    else:
        if root.left:
            f(root.left, path, all_paths)
        if root.right:
            f(root.right, path, all_paths)
    path.pop()


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        res = []
        f(root, [], res)
        return res
