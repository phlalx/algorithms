#TAGS tree

# nice exercise, seems easy now that it's done

class Solution:
  def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
    adj = {}
    
    def dfs(node, par):
      if not node:
        return
      adj[node.val] = [n.val for n in [par, node.left, node.right] if n]
      dfs(node.left, node)
      dfs(node.right, node)
        
    dfs(root, None)

    queue = deque([target.val])
    res = []
    seen = {target.val:0}
    while queue:
      x = queue.popleft()
      d = seen[x]
      if d > k:
        continue
      if d == k:
        res.append(x)

      for xx in adj[x]:
        if xx not in seen:
          seen[xx] = d + 1
          queue.append(xx)
      
    return res
