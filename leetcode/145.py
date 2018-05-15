#TAGS tree, classic
# similar for inorder/preorder/postorder
#
# Trick: stack up node remaining to be visited
#  reason on `while st: x = st.pop()` where x
#  is the first element to be displayed
#  then see how to maintain the stack invariant, and initialize the stack

class Solution:
  def postorderTraversal(self, root: TreeNode) -> List[int]:
    res = []
    st = []
    
    def stackup(node):
      while node:
        st.append(node)
        node = node.left or node.right
    
    stackup(root)
    while st:
      x = st.pop()
      if x.right is None or x.right is last:
        res.append(x.val)
        last = x
      else:
        st.append(x)
        stackup(x.right)
      
    return res
        
