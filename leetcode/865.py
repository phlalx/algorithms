#TAGS tree
#  trick: don't think in terms of finding deepest leaves + LCA, but find
#  recursive solution. We simply need to compute the height of a tree
#  and compare heights of left/right trees

class Solution:
  def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
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
      
    
