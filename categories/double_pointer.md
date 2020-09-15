# Double pointers / Sliding windows

A lot of program require to enumerate pairs, subarrays, or substrings that
enjoy some property `P`. The problem usually boildowns to traversing 
an implicit matrix.

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

# Computing `P(i, j)`

In the simplest cases, `P(i, j)` is a function of `T[i]` and `T[j]`. In more
difficult problems, `P(i, j)` is a function of the values in `T[i:j+1]`.
In that latter case, we can compute `P(i, j)` from `P(i,j-1)` and `P(i-1,j)`
and possibly some state.

# Implementation hints

There are two ways of enumerating non-empty substrings
(increasing left index or right index, which corresponds to traversing the
 matrix line-first or column-first).

```
for j in range(n):
    for i in range(0, j+1):
        if prop(i, j):
            process(i,j)
```

```
for i in range(n):
    for j in range(i, n):
        if prop(i, j):
            process(i, j)
```

This isn't indifferent. While the second one seems more natural, the first
one can make things easier when computing `prop(i, j)` incrementally.

# Example of monotonicity

* Substrings with unique letters `P(i, j) => P(ii, jj) if ii >= i and jj <= j)`

```
a b c c b a
1 1 1 0 0 0
  1 1 0 0 0
    1 0 0 0
      1 1 1
        1 1
          1
```

* Substrings containing all three characters `a, b, c`

```
a b c d c b a
0 0 1 1 1 1 1
  0 0 0 0 0 1
    0 0 0 0 1
      0 0 0 1
        0 0 1
          0 0
            0
```

* Non-monotonicity, substring with exactly three characters `a, b, c`

```
a b c d c b a
0 0 1 0 0 0 0
  0 0 0 0 0 0
    0 0 0 0 0
      0 0 0 0
        0 0 1
          0 0
            0
```

# Taking advantage of the monotonicy propery

From such a matrix, we can enumerate all pairs that satisfy `P`,
count them, return the longest/shortest substrings, check for existence of
a pair.

When the matrix has good *monocity properties*, we can answer some of these
questions in linear time. This defines the class of *double pointer*
problems. In these problems, we usually traverse the (implicit) matrix by
incrementing at least `i` or `j` at each iteration. Sliding windows are
double pointers problems where pairs `(i, j)` are interpreted as subarrays
or substrings.

Note that enumerating pairs is always `O(n**2)` regardless of the
monotonicity so usually problems don't ask for enumerations.


Thanks to the monotonicity property, we don't need to scan the full matrix.
We can stop as soon as the property hold (or doesn't hold), and don't need
to reset `i`.

## Example 1: longest substrings with unique chars !3

```
a b c c b a
1 1 1 0 0 0
  1 1 0 0 0
    1 0 0 0
      1 1 1
        1 1
          1
```

```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = []
        i = 0
        res = 0
        prop = True
        for j in range(n):
            seen.append(s[j])
            while len(seen) != len(set(seen)):
                seen.remove(s[i])
                i += 1
            res = max(res, j-i+1)
        return res
```

TODO: in that case, it's easier to traverse by line first
```
def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    j = 0
    best = 0
    seen = set()
    for i in range(n):
        while j < n and s[j] not in seen:
            seen.add(s[j])
            j += 1
        best = max(best, j - i)
        seen.remove(s[i])
    return best
```

## Example 2: count substring with at least three characters !1358

```
a b c d c b a
0 0 1 1 1 1 1
  0 0 0 0 0 1
    0 0 0 0 1
      0 0 0 1
        0 0 1
          0 0
            0
```

For each column `j` from left to right, find the first `i` such that `P(i, j)`
doesn't hold.

```
def numberOfSubstrings(s):
    n = len(s)
    def prop(i, j):
        return all(c in s[i:j+1] for c in 'abc')
    i = 0
    res = 0
    for j in range(n):
        while prop(i, j):
            i += 1
        res += i
    return res
```

Same algorithm, but compute `prop` incrementally
TODO: could we compute `prop` incrementally if we traverse by line first?

```
def numberOfSubstrings(s) -> int:
    n = len(s)
    count = {'a': 0, 'b': 0, 'c': 0}
    def prop(i, j):
        return all(count.values())
    i = 0
    res = 0
    for j in range(n):
        count[s[j]] += 1
        while prop(i, j):
            count[s[i]] -= 1
            i += 1
        res += i
    return res
```

# Some leetcode problems

Number of Substrings Containing All Three Characters !1358 (count / increasing)
longest substring without repeating characters !3 (longest / decreasing)
Permutation in String !567

Count Number of Nice Subarrays !1248
Replace the Substring for Balanced String
Max Consecutive Ones III
Binary Subarrays With Sum
Subarrays with K Different Integers
Fruit Into Baskets
Shortest Subarray with Sum at Least K
Minimum Size Subarray Sum

# Difference with DP (TODO improve this section)

* DP is usually `O(n^2)`
* we compute a function instead of a predicate
* we scan the whole matrix

# Trick

* number of string with exactly k something = (num >= k) - (num >= k + 1) !1248
 

