
When sorting an array `A`, we apply a permutation `sigma`.

The expression
```
sorted(range(len(A)), key=A.__getitem__)
```
applies the same permutation to list `[0,1,...,n-1]`. The reason is that
`0` is treated as `A[0]`, `1` as `A[1]` and so on.

Suppose we have two arrays of equal size, `A` and `B`. We want to apply
 to `B` the permutation that makes `A` sorted.

```
sorted(enumerate(B), key= lambda x: A.x[0])
```

See exercise 870.

