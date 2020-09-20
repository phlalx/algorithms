# TAGS tree, traversal, classic, data structure, cool
# SEE ALSO 94
#
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def push_left(st, node):
    while node:
        st.append(node)
        node = node.left

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.st = []
        push_left(self.st, root)


    def next(self) -> int:
        """
        @return the next smallest number
        """
        n = self.st.pop()
        res = n.val
        if n.right:
            push_left(self.st, n.right)
        return res

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return bool(self.st)

# Another cool solution (but more complicated)
# 
# def bst_min(root):
#   while root.left:
#     root = root.left
#   return root
# 
# def successor(root, node):
#   if node.right:
#     return bst_min(node.right)
#   res = None
#   cur = root
#   while cur is not node:
#     if node.val <= cur.val :
#       res = cur
#       cur = cur.left
#     else:
#       cur = cur.right
#   return res
# 
# class BSTIterator:
# 
#     def __init__(self, root: TreeNode):
#       self.root = root
#       self.cur = bst_min(root) if root else None
# 
#     def next(self) -> int:
#       res = self.cur.val
#       self.cur = successor(self.root, self.cur)
#       return res
# 
#     def hasNext(self) -> bool:
#       return self.cur is not None
# 
