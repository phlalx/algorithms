# Tree

In python
```
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right
```

Careful with base case. `None` is not a tree.

```
type t =
  | Node of int * t * t
  | None

let rec height =
   | None _ -> -1
   | Node _, t1, t2 -> 1 + max (height t1) (height t2)
```


Sometimes, it easier to stop recursion at leave.

```
type t =
  | Bin of int * t * t
  | Left of int * t
  | Right of t * int
  | Leaf of int
```


def is_valid(t):
    if t.left is None and t.right is None:
        return True, t.val, t.val
    elif t.left is None:
        rval, rmin, rmax = is_valid(t.right)
        return rval and rmin >= t.val, t.val, rmax
    elif t.right is None:
        lval, lmin, lmax = is_valid(t.left)
        return lval and t.val >= lmax, lmin, t.val
    else:
        rval, rmin, rmax = is_valid(t.right)
        lval, lmin, lmax = is_valid(t.left)
        return lval and rval and lmax <= t.val <= rmin, lmin, rmax

## Diameter

### of a binary tree

### of a general tree

. 2 dfs
. Take any vertice v
. Find longest path from v, it  gives you a leaf x
. Find longest path from x, it gives you another leaf y
. x -> y is a diameter of the tree

Proof:
. Suppose x -> y is a diameter and show it can be constructed
  by the given procedure
. pick somme v
. Let's root the tree in v
. We want to show that x or y is the further node from v
. 2 cases
  . v in path(x, y). In that case, v -> x or v -> y is
    the longest path from v (otherwise we could construct a
    longer path.
  . v not in path(x, y).
        suppose x, y are not further leaves
        let z the further leaf from v
        let t = LCA(x,y)
        we can construct a longer path (few cases to consider...
        TODO)


# Definition of a tree
G is a graph with n vertices.
It is a tree if any two properties hold
. n - 1 edges
. connected
. no cycle

# Counting trees

Binary tree = catalan number  = 4 ^ n
General tree = n ^ (n - 2)
Graph = 2 ^ (n * (n-1) / 2)











