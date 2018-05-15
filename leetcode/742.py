#TAGS tree
# tricky

# Two types of solutions
# 1. One way is turn tree into a graph (see 863)
# 2. Other way is to walk tree, to tedious, not the right approach

#
# Initial solution (2) tedious and wrong anyway because I return the
# length of the path and not the leaf
#
class Solution:
  def findClosestLeaf(self, root: TreeNode, k: int) -> int:
    def dfs(node) -> Tuple[int, int, int, bool]:
    # -> height, depth_k, height_k, contain_k
      if node is None:
        return -1, None, None, False
      lh, ldk, lhk, lcontaink = dfs(node.left)
      rh, rdk, rhk, rcontaink = dfs(node.right)
      
      h = 1 + min(lh, rh)
      
      dk = None
      if ldk is not None:
        dk = ldk + 1 
      elif rdk is not None:
        dk = rdk + 1 
      elif node.val == k:
        dk = 0
       
      containk = lcontaink or rcontaink or node.val == k
      if lcontaink:
        hk = lh
      elif rcontaink:
        hk = rh
      elif node.val == k:
        hk = h
      else:
        hk = None
      print(node, h, dk, hk, containk)
      return h, dk, hk, containk
    
    h, dk, hk, _ = dfs(root)
    return min(h, dk + hk)

# Second attempt at solution 2 (still some bug, not worth debugging)
# this isn't the right approach for this problem
      
def minPath(node):
  depth = float('inf')
  res = None
  def dfs(node, level):
    nonlocal res, depth
    if node is None:
      return
    if node.left is None and node.right is None and level < depth:
      res = node
      depth = level
    dfs(node.left, level+1)
    dfs(node.right, level+1)
  dfs(node, 0)
  return res, depth

def findNode(node, level, k):
  if node is None:
    return None, None
  if node.val == k:
    return node, level
  lnode, ldepth = findNode(node.left, level+1, k)
  rnode, rdepth = findNode(node.right, level+1, k)
  if lnode:
    return lnode, ldepth
  else:
    return rnode, rdepth

class Solution:
  def findClosestLeaf(self, root: TreeNode, k: int) -> int:
    nodek, depthk = findNode(root, 0, k)
    leafk, depthleafk = minPath(nodek)
    leafall, depthleafall = minPath(root)
    if depthleafk < depthleafall + depthk:
      return leafk.val
    else:
      return leafall.val

# This is a much simpler solution
# Actually, the constraint that all node.val are unique is a hint
# hint to use a graph
#

from collections import deque

class Solution:
  def findClosestLeaf(self, root: TreeNode, k: int) -> int:
    adj = {}

    def dfs(node, par):
      if not node:
        return
      adj[node.val] = [n.val for n in [par, node.left, node.right] if n]
      dfs(node.left, node)
      dfs(node.right, node)

    dfs(root, None)

    # Corner case, root is not a leaf (except when it is)
    isleaf = lambda x: not adj[x] or len(adj[x]) == 1 and x != root.val

    queue = deque([k])
    # don't forget to keep track of seen, this is an undirected graph,
    # not a tree!
    seen = {k}
    while queue:
      x = queue.popleft()
      neigh = adj[x]
      if isleaf(x):
        return x
      for xx in neigh:
        if xx not in seen:
          seen.add(xx)
          queue.append(xx)

