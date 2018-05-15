#TAG tree
# yet another tree problem
# do it on paper first to see if we use synth/inherited attributed and how
# to deal with None
#
# If we don't recurse to None, don't forget to deal with corner case where
# root = None.
#  
# In this example, we don't recurse through None because we need
# node.left, node.right value
#

class Solution:
  def longestConsecutive(self, root: TreeNode) -> int:
    res = float('-inf')
    def f(node) -> Tuple[int, int]:  # longest increasing sequence starting/end
      nonlocal res
      v = node.val
      linc, rinc, ldec, rdec = (1,) * 4
      
      if node.left is not None:
        linc, ldec = f(node.left)
        if v == node.left.val - 1:
          linc += 1
        else:
          linc = 1
        if v == node.left.val + 1:
          ldec += 1
        else:
          ldec = 1
          
      if node.right is not None:
        rinc, rdec = f(node.right)
        if v == node.right.val - 1:
          rinc += 1
        else:
          rinc = 1
        if v == node.right.val + 1:
          rdec += 1
        else:
          rdec = 1
      
      res = max(res, linc + rdec - 1, rinc + ldec - 1) 
      return max(linc, rinc), max(ldec, rdec)
      
    if root is None:
      return 0
    f(root) 
    return res
      
