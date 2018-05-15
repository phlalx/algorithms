# Tips

* Most tree problems are variants of dfs
* See if `dfs` function use:
  - synthetized attributes
  - inherited attributes
  - global variable 

* See what is the base case that ends recursion
  - Usually we use `None` as left/right trees for leaves

Two patterns

```
def dfs(node):
  if node is None:
      return ...
  a = dfs(node.left)
  b = dfs(node.right)
  return f(a, b)
```

```
def dfs(node):
    if node.left is None and node.right is None:
        return ...
    if node.left:
        a = dfs(node.left)
    else:
        a = ...
    if node.right:
        b = dfs(node.right)
    else:
        b = ...
    return f(a, b)
```

First case work most of the time and is easier but not always possible.
Consider for instance: returning a leaf with a given property. When we
 reach `None`, we don't have anything to return.

In seconde case, don't forget to test the corner case where root is None.

Also it often helps to use a global variable

```
res = ...
def dfs(node):
  if node is None:
      return
  dfs(node.left)
  dfs(node.right)
  res = f(res, node.val)
```
