#TAGS tree, linked list
# cool, TODO  think simpler + iterative

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        def f(root):
            old_right = root.right
            if root.left is not None:
                left_last = f(root.left)
                root.right = root.left
                root.left = None
            else:
                left_last = root
            left_last.right = old_right
            
            if old_right is not None:
                last = f(old_right)
            else:
                last = left_last
            
            return last
        f(root)
