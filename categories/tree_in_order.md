# Iterative in-order traversal of a tree (94)

* Trick find the right loop invariant.
* Stack is non-empty. Left side of node on top of the stack is None or
  has been processed already.

```
def push_all_left(stack, node):
    while node:
        stack.append(node)
        node = node.left

def f(root):
    res = []
    stack = []
    push_all_left(stack, root)
    while stack:
        # process first node of the stack
        node = stack.pop()
        res.append(node.val)
        # stack up all left nodes
        if node.right:
            push_all_left(stack, node.right)
    return res
```
