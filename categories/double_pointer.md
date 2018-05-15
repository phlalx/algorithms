# Double pointers

A lot of program require to enumerate pairs, subarrays, or substrings that
enjoy some property `P`. This can be representated as a matrix.

## Example 1

Consider `P(i, j) = sum(T[i:j+1]) >= 10`

```
1 2 3 4 5 6 7
F F F T T T T
  F F F T T T
    F F T T T
      F F T T
        F T T
          F T
            F
```

## Example 2

Well-formed parenthesis substring

```
( ) ( ) ) ( ( ) )
F T F T F F F F F
  F F F F F F F F
    F T F F F F F
      F F F F F F
        F F F F F
          F F F T
            F T F
              F F
                F
```

## Example 3

`P(i, j) = i + j >= 10`

```
1 2 3 4 5 6 7
F F F F F F F
  F F F F F F
    F F F F T
      F F T T
        T T T
          T T
            T
```

## Example 4

`P(i, j) = i + j == 10`

```
1 2 3 4 5 6 7 8
- - - - - - - -
  - - - - - - T
    - - - - T +
      - - T + +
        T + + +
          + + +
            + +
              +
```

## Display the matrix in Python

```
l = [1,2,3,4,5,6,7]
pred = lambda i, j: int(i + j >= 10)

for v in l:
    print ([ pred(u, v) for u in l ])
```

# Sliding windows, double pointers

From this matrix, we can enumerate all pairs, count them, return the
longest/shortest ones, check for existence. When the matrix has good
monocity properties (looks like a half-plane), we can usually answer
some of these questions in linear time using sliding windows or double pointers.

Typicall, enumeration would be `O(n**2)` so usually the problems
don't ask that enumerations, because it would cancel the benefits of
the window.

TODO difference between sliding windows and dubole pointer

# Computing `P(i, j)`

In the simplest cases, `P(i, j)` is a function of `T[i]` and `T[j]`. In more
difficult problems, `P(i, j)` is a function of the values in `T[i:j+1]`.
In that latter case, we can compute `P(i, j)` from `P(i,j-1)` and `P(i-1,j)`
and possibly some state.

# Difference with DP

* DP is usually `O(n^2)`
* we compute a function instead of a predicate
* we scan the whole matrix


# Example

think of enumerating intervals
```
for j in range(n):
    for i in range(j, n+1):  # interval of the form [i,j)
        if prop(i,j):
            process(i,j)
```

We can do better thanks to the monotonicity property.
We can stop as soon as the property doesn't hold
and no need to reset j.

```
i = 0

for j in range(n):
    while i <= n and prop(i, j):
        process(i, j)
        i += 1
```

In the final version, we compute `prop` gradually.

```
i = 0
prop = True  #  (prop(0, 0))

for j in range(n):
    while i <= n and prop:
        process(i, j)
        i += 1
        update(prop, i)  # take into account addition of i
    update(prop, j)  # take into account removal of j
```


Sliding window problems
-----------------------
Number of Substrings Containing All Three Characters
Count Number of Nice Subarrays
Replace the Substring for Balanced String
Max Consecutive Ones III
Binary Subarrays With Sum
Subarrays with K Different Integers
Fruit Into Baskets
Shortest Subarray with Sum at Least K
Minimum Size Subarray Sum

