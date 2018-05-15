# TAGS binary tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = Noneo


def traverse(tree, levels, level):
    if tree is None:
        return
    levels.setdefault(level, []).append(tree.val)
    traverse(tree.left, levels, level + 1)
    traverse(tree.right, levels, level + 1)
    return levels


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        items = list(traverse(root, {}, 0).items())
        items.sort(key=lambda x: x[0])
        return [v for (i, v) in items]
