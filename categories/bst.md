# Binary Search Tree

* lookup can be recursive/iterative, iterative is easier to implement
* insertion is always at the leaves


```
class Bst:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

```
def lookup(bst, x):
    while bst:
        if bst.val == x:
            return bst
        # write inequality in this direction
        # less surprise
        elif x <= bst.val:
            bst = bst.left
        else:
            bst = bst.right
    return None
```

```
# recursive/immutable insert
def insert(bst, x):
    if bst is None:
        return Bst(x)
    if x <= bst.val:
        return Bst(bst.val, insert(bst.left, x), bst.right)
    else:
        return Bst(bst.val, bst.left, insert(bst.right, x))
```

Iterative is slightly harder
```
def insert(node, x):
    bst = node
    leaf = TreeNode(x)
    if bst is None:
        return leaf
    parent = None
    while bst:
        if x <= bst.val:
            parent = bst
            bst = bst.left
        else:
            parent = bst
            bst = bst.right
    if x <= bst.val:
        parent.left = leaf
    else:
        parent.right = leaf
    return node
```

