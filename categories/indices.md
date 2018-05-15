# Some notes about indices manipulations

## Divide and conquer

Suppose `I = [i, j]` with `i != j`

We divide the interval in two parts `[i, m]` and `[m', j]`.
where `m = (i + j) // 2` and `m' = m + 1`.

0  1  2  3
   m  m'

0  1  2  3  4
      m  m'

The second half is never larger than the first part.

## Find a sub-array with elements in [lo, hi]

`l` is a list.

```
n = len(l)
i = 0
while i < n and l[i] < lo:
    i += 1
j = i
while j < n and l[j] <= hi:
    j += 1
```

`l[i]` is the first element such that `l[i] >= lo`.
`l[j]` is the first element such that `l[j] > hi`.
So the result is `l[i:j]`.

Note that it works even if l is empty.
