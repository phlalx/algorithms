# TAGS tree, same as 863
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
    def walk(node) -> Tuple[TreeNode, int]:  # height + solution
      if node is None:
        return None, -1
      lsol, lheight = walk(node.left)
      rsol, rheight = walk(node.right)
      if lheight == rheight:
        return node, lheight + 1
      elif lheight < rheight:
        return rsol, rheight + 1
      else:
        return lsol, lheight + 1
    return walk(root)[0]


