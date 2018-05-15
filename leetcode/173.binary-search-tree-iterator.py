# TAGS tree, traversal, classic, data structure, cool
# SEE ALSO 94
#
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.cur = root  # next subtree to process
        self.branch = []  # stack of nodes to process after dealing with cur

        # stack up all the left-most branch
        while self.cur:
            self.branch.append(self.cur)
            self.cur = self.cur.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.branch

    def next(self):
        """
        :rtype: int
        """
        # stack up all the left-most branch
        n = self.branch.pop()

        self.cur = n.right
        res = n.val

        while self.cur:
            self.branch.append(self.cur)
            self.cur = self.cur.left

        return res


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
