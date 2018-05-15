

# mental image
#
#
#(left) Dummmy (right) -> (left) node1 (right) ->
#   |                                             |
#    ---------------------------------------------- 
#
# One class Node is enough. We could use two.
#
# This implementation uses a plain data object, but we could use methods
# instead of function. For instance if we want to keep the size of list
# 
# Important trick
#   write insert_after and remove, everything else just follows.
#


class Node:
  def __init__(self, k=None, v=None):
    self.k = k
    self.v = v
    self.left = self
    self.right = self

# insert_after and remove are the two functions that we can use as
# building blocks for all the other ones
def insert_after(node, new_node):
  new_node.right = node.right
  new_node.left = node
  node.right.left = new_node
  node.right = new_node

def remove(node):
  node.left.right = node.right
  node.right.left = node.left
  return node

def appendleft(dq, k, v):
  nn = Node(k, v)
  insert_after(dq, nn)

def pop(dq):
  return remove(dq.left)

def movetofront(dq, n):
  remove(n)
  insert_after(dq, n)
