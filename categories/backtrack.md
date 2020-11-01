# Backtracking

Build a set of solutions by dfs an implicit tree. Each solution is a leaf
of the tree, and can be constructed step by step by traversing the path
from the root to the leaf.

This can be seen as brute force approach where constraints on the solutions
allow us to prune some sub-trees.

## Applications

* Generate all permutations
* generate all subsets of a set
* generate all queens position
* generate all solutions of a sudoku grid.

## Example: generate all well-formed parentheses (leetcode 22)

```
# Dumb backtracking generation of all parenthesis expressions
# *without* the parenthesis matching constraint.
def generateParenthesis(self, n):
    cur = []  # the string being built
    res = []

    def f(i):
        if i == 2 * n:
            res.append(''.join(cur))
        else:
            cur.append('(')
            f(i+1)
            cur.pop()
            cur.append(')')
            f(i+1)
            cur.pop()

    f(0)
    return res
```

We start from this dumb algorithm, and a constraint to ensure we only
add closing parenthesis if there's an open one before.

See also 282 for a slightly more complex problem with
some notes.

## Notes

* The shape of the solution is always the same.
* We maintain an "ongoing" global solution, that we construct/deconstruct, and
  we print/store it when reaching the leaf. In theory, it could be passed as
  a parameter but it would too costly.
* backtracking vs dfs
    - backtracking: general exploration algorithm of a solution space.
                    (dfs, with pruning, usually implicit search tree)
    - dfs: recursive dfs (graph or tree) is a particular backtracking
           algorithm.