#TAGS tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def walk(root, depth):
            if root is None:
                return float('inf')
            res = min(walk(root.right, depth+1), walk(root.left, depth+1))
            if res == float('inf'):
                return depth
            else:
                return res
        if root is None:
            return 0
        return walk(root, 0) + 1
        
