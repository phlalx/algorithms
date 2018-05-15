# Counting

## Catalan numbers

C(n) = sum( c(n-1-i) * c(i) for i in range(n) )
     = 1 / (n+1) * C(2*n, n)

## Application

C(n) is the number of:

### well-parenthesed expression of size 2*n

the right way to see it is to partition expressions like this

```
    C0 = { '' }
    Cn =
       ( C_n-1 ) C_0
       ( C_n-2 ) C_1
       ( C_n-3 ) C_2
       ...
       ( C_0 ) C_n-1
```

Said differently, we partition over the length of the first parenthesis.

Mistakes that I did:
And not `C(n-i) * C(i)` because this doesn't correspond to a partition,
we would count two times `()()()`.
It would be wrong also to try to count all expressions of the form
`( exp1 ) ( exp2 )`. We would miss `()()()`.

### unique paths that don't cross the diagonal in a `n * n` grid,

Isomorphic to parenthesis.

### Number of ways to desambiguate a product of `n + 1` factors

```
product = x_0 * ... * x_n
```

We have n points to split the product.

```
x_0 * x_1 * ... * x_i-1 * x_i * ... * x_n
    0     1                        n-1

C_n = sum(c_i * c_n-1-i)   # TODO check this
```

### Binary trees

`C_n` is the number of binary tree with n nodes
`C_n` is the number of full binary trees with `n+1` leaves (or `2n + 1` nodes)

There is a bjiection between full binary trees with `2n+1` nodes, and
regular binary tree with n nodes.

* See !894
* https://stackoverflow.com/questions/54498134/number-of-full-binary-trees
* https://www.whitman.edu/mathematics/cgt_online/book/section03.05.html


## Asymptotic behavior

```
C(n) ~ 4 ^ n / n ^ x (via Stirling)
```

## Leetcode

See !22
