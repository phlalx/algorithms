# Dynamic programming

Technique to solve problems that enjoy the optimal substructure property.

A problem has the optimal substructure property if:
* if an instance s of the problem has a solution f(s) iff at least
  some s' has a solution f(s').

We can then construct `f(s) = F( f(s') for s -> s')`.

The relation `->` must form a DAG. We can compute `f(s)` recursively, and
memoize intermediary results (`s -> f(s)`). Very often, `F` is a min or max.

## BFS

A simpler class of such problems are those where
`f(s) = min (1 + f(s') for s -> s')`.

Example: `279.perfect-squares`

In that case, it's more efficient to use A BFS.

TODO: I wonder if we can also use dijkstra in certain cases.

## Computing the set of results

Some problems ask for the set of results. For instance, in perfect squares,
return the squares that give the result. Or for the longest increasing
subsequence, return the actual sequence, and not only its length.

There are several ways to do it.
* store the solution in the memo table (easy if there is a unique solution
  and if the solution is rather small - like an int, and not a path)
* store the the states that lead to a solution in the memo table.
`s -> f(s), {s', s'',....}`. This gives the DAG of solution.
* rewrite another implem of the recursive dp function but explore only
  those states that gave the solution
* Or forgot about dp altogether and use a backtracking approach with no
  memoization. Walk the dag and print all the paths that lead to a solution.
  This may work because displaying all paths may defeat the purpose of
  memoization.

# Cool problem

689





