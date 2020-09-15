# Kth elements

Find the kth elements of a list of numbers (or the k first elements).
There are several solutions.

## Sorting

Easy to implement but not the most efficient `O(n.log(n))`. Another
advantage is that it is the only stable solution.

## Max heap

Better than sorting `O(n.log(k))`. The naive idea to push all the elements
in a heap, then pop the first `k` elements is incorrect. Instead, we
bound the heap size to `k` and use a *max heap*. Whenever the heap size
is `k+1`, we pop the largest (first) element. Hence we are garanteed that
the heap contains the `k` smallest elements at all time.

It works also for streams of values.

## k-select

This is faster `O(n)` on average, `O(n**2)` worst case. It's harder to
implement.

## binary search

If we can count how many elements are strictly smaller than a given element

```
count(v) = #{vv | vv <= v}
```

We can find the kth element by binary search. The kth element is the smallest
element `v` such that `count(v) >= k`.

Example:
```
   1  2  3  4  4  4  4  5

k = 0    v = 1  (count(v) = 0)
k = 1    v = 2  (count(v) = 1)
k = 2    v = 3  (count(v) = 2)
k = 3    v = 4  (count(v) = 6)
k = 4    v = 4  (count(v) = 6)
k = 5    v = 4  (count(v) = 6)
k = 6    v = 4  (count(v) = 6)
k = 7    v = 5  (count(v) = 7)
```

See !668.

## Merge

kth element of n sorted lists can be obtained by n-merge. See !378.



