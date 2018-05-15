# TAGS tree


def is_leaf(tree):
    return tree and not tree.left and not tree.right


def sum_left_leaves(tree, isLeft):
    if not tree:
        return 0
    if is_leaf(tree) and isLeft:
        return tree.val
    return sum_left_leaves(tree.left, True) + sum_left_leaves(tree.right, False)


class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return sum_left_leaves(root, False)
