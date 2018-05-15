#TAGS tree
# follow up to 98

def f(node) -> Tuple[TreeNode, int, int, int]:  # largest_bst, mi, max, size
  if not node:
    return None, float('inf'), float('-inf'), 0
  lbst, lmi, lma, lsize = f(node.left)
  rbst, rmi, rma, rsize = f(node.right)
  if lbst == node.left and rbst == node.right and lma < node.val < rmi:
    bst = node
    size = 1 + lsize + rsize
    mi = min(lmi, rmi, node.val)
    ma = max(lma, rma, node.val)
    return bst, mi, ma, size
  elif lsize < rsize:
    return rbst, rmi, rma, rsize
  else:
    return lbst, lmi, lma, lsize
  
        
class Solution:
  def largestBSTSubtree(self, root: TreeNode) -> int:
    return f(root)[3]
   
