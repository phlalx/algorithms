#TAGS tree
# easy with dfs, more tricky with constant space
# see 429 

class Solution:
  def connect(self, root: 'Node') -> 'Node':
    l = []
    def dfs(node, level):
      if len(l) == level:
        l.append(None)
      node.next = l[level]
      l[level] = node
      if node.right:
        dfs(node.right, level + 1)
      if node.left:
        dfs(node.left, level + 1)
    if root is None:
      return None
    dfs(root, 0)
    return root

# constant space
# trick: use next pointers from previous level
#
# write loop for one level only, and expand to full algo

class Solution:
  def connect(self, root: 'Node') -> 'Node':
    if not root:
        return root
    dummy = Node()
    pre = dummy
    node = root
    next_line = node.left
    while node and next_line:
      pre.next = node.left
      node.left.next = node.right
      pre = node.right
      node = node.next
      if not node:
        node = next_line
        next_line = node.left
        pre = dummy
    return root


