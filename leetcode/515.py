#TAGS tree
# easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        largest = []
        def dfs(node, level):
            if node is None:
                return
            if len(largest) == level:
                largest.append(node.val)
            else:
                largest[level] = max(largest[level], node.val)
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root, 0)
        return largest
                
        
