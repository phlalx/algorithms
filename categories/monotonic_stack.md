# Monotonic stack/queue

## General ideas

Scan an array, remember most recent greater/smallest element.

Best seen on a picture:

Suppose given an array `l = [4, 1, 3, 2, 1]`

```
X
X     X
X     X  X
X  X  X  X  X
0  1  2  3  4
```

While scanning the array, we can build a strictly decreasing subsequence:

```
X
X  X
X  X  X
X  X  X  X
0  2  3  4
```
i = 4 is the most recent max
i = 3 is the second most recent max
i = 2 is the third most recent max
i = 0 is the last most recent max

```
st = []
for i, v in enumerate(l):
    while st and l[st[-1]]  <= v:
        st.pop()
    st.append(i)
```

Or similarly a strictly increasing subsequence

```
X
4
```

```
st = []
for i, v in enumerate(l):
    while st and l[st[-1]]  >= v:
        st.pop()
    st.append(i)
```

## Some observations

* We store indices and not values, this is more general
* Complexity is linear (each element is store exactly once, and pop at most once)
* We always store the last elements

## Types of problems

# Leetcode problems

496 Next Greater Element I
239 Sliding Window Maximum

42 Trapping Rain Water
84 Largest Rectangle in Histogram
316 Remove duplicate letters
321 Create maximum number
402 Remove K digit
503 Next Greater Element II
856 Score of Parentheses
901 Online Stock Span
907 Sum of Subarray Minimums
1081 Smallest Subsequence of Distinct Letters
1130 Minimum Cost Tree From Leaf Values
