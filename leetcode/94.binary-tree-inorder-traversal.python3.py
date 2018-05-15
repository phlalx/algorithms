# TAGS tree, traversal, cool, trick
# TODO redo

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def push_all_left(stack, node):
    while node:
        stack.append(node)
        node = node.left


def f(root):
    res = []
    stack = []
    push_all_left(stack, root)
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            push_all_left(stack, node.right)
    return res


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return f(root)
