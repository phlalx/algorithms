# Binary search has several variations.
# - search for a value, or a value that satisfies a predicate
# - return a boolean or an index,
# - return as possible or go through all the recursion.
# - do we use inclusive or exclusive bounds.
# - if the value appears several times in the array, which index do we return

import bisect

# note: it's important to test arrays of odd and even length!
l = [1, 2, 3, 4, 4, 4, 5, 7, 7]

# return index where element should be, provided we shift everything to the
# right. This can be outside the array, index = n
# bisect_left and bisect_right give different results when the element
# is in the array
assert bisect.bisect_left(l, 4) == 3  # index of first occurence  of 4
assert bisect.bisect_right(l, 4) == 6  # index right after first occurence of 4
assert bisect.bisect_right(l, 8) == len(l)
assert bisect.bisect_left(l, 8) == len(l)
assert bisect.bisect_left(l, 0) == 0
assert bisect.bisect_right(l, 0) == 0
assert bisect.bisect_left(l, 1) == 0
assert bisect.bisect_right(l, 1) == 1

# The version which returns an index is more general than the one that
# returns a boolean

def is_in(nums, v):
    k = bisect.bisect_left(nums, v)
    return k < len(nums) and nums[k] == v

# Unfortunately, bisect isn't quite general in python, it misses a `pred`
# parameter. We often have to re-implement it.
# 

# Version 1 (simplest)

# inclusive bounds
# search existence of element
# go through all the recursion
def binary_search(l, elt, i, j):
    while i != j:
        m = (i + j) // 2
        assert i <= m < m + 1 <= j #  true only if i < j
        if elt <= l[m]:
            j = m
        else:
            i = m + 1
    return l[i] == elt

assert binary_search(l, 1, 0, len(l) - 1)
assert binary_search(l, 2, 0, len(l) - 1)
assert binary_search(l, 4, 0, len(l) - 1)
assert not binary_search(l, 0, 0, len(l) - 1)
assert not binary_search(l, 8, 0, len(l) - 1)
assert not binary_search(l, 6, 0, len(l) - 1)

# Version 2
# inclusive bounds
# search existence of element
# stop as soon as possible
# faster but just a little trickier to code, better to avoid
# We cut the interval in three parts, which leads to possibly
# two base cases, empty interval, and singleton
def binary_search_2(l, elt, i, j):
    # careful with this termination condition, it could be i == j or i == j - 1
    while i < j:
        m = (i + j) // 2
        assert i <= m < m + 1 <= j
        if elt == l[m]:
            return True
        elif elt < l[m]:
            j = m - 1
        else:
            i = m + 1
    return elt == l[i]

assert binary_search_2(l, 1, 0, len(l) - 1)
assert binary_search_2(l, 2, 0, len(l) - 1)
assert binary_search_2(l, 4, 0, len(l) - 1)
assert not binary_search_2(l, 0, 0, len(l) - 1)
assert not binary_search_2(l, 8, 0, len(l) - 1)
assert not binary_search_2(l, 6, 0, len(l) - 1)

# Version 3

# Same as version 1 but with exclusive right bound
# exclusive bounds
# search existence of element
# go through all the recursion
def binary_search_3(l, elt, i, j):
    # be careful with this bound
    # we want to stop when len([i,j)) = j - i = 1
    while i + 1 < j:
        m = (i + j) // 2
        assert i <= m < m + 1 <= j #  true only if i < j
        # we split in [i,m) [m,j)
        # if elt == l[m], we need to look up in right half
        if elt >= l[m]:
            i = m
        else:
            j = m
    return l[i] == elt

assert binary_search_3(l, 1, 0, len(l))
assert binary_search_3(l, 2, 0, len(l))
assert binary_search_3(l, 4, 0, len(l))
assert not binary_search_3(l, 0, 0, len(l))
assert not binary_search_3(l, 8, 0, len(l))
assert not binary_search_3(l, 6, 0, len(l))

# Version 4
#
# bisect_left, based on version 1
#
def binary_search(l, elt, i, j):
    while i != j:
        m = (i + j) // 2
        assert i <= m < m + 1 <= j #  true only if i < j
        if elt <= l[m]:
            j = m
        else:
            i = m + 1
    assert i in range(len(l))
    # CAREFUL consider all cases, most of the time, answer is i
    # if elt in l, i is the leftmost such element because we always look
    # in priority in the left part.
    # Suppose l = [1, 2, 4 ,6], and we lookup 3
    # l[m] = 2, l[m+1] = 4, we will lookup in [4, 6],
    #    eventually returns (index of) 4
    # Suppose l = [1, 2, 4, 6], and we lookup 7, return (index of 6)
    if l[i] >= elt:
        return i
    else:
        return len(l)

def my_bisect_left(l, elt):
    assert l
    i = 0
    j = len(l) - 1
    return binary_search(l, elt, i, j)

# return place where element should be (possibly outside array, index = n)
assert bisect.bisect_left(l, 4) == my_bisect_left(l, 4)
assert bisect.bisect_left(l, 8) == my_bisect_left(l, 8)
assert bisect.bisect_left(l, 0) == my_bisect_left(l, 0)
assert bisect.bisect_left(l, 1) == my_bisect_left(l, 1)

# Version 5
#
# bisect_right
#
def binary_search(l, elt, i, j):
    while i != j:
        m = (i + j) // 2
        assert i <= m < m + 1 <= j #  true only if i < j
        if elt >= l[m+1]:
            i = m + 1
        else:
            j = m
    assert i in range(len(l))
    # CAREFUL, consider all cases, most of the time answer is i + 1yy
    # if elt in l, i is the rightmost such element because we always look
    # in priority in the right part in case of equality.
    # Suppose l = [1, 2, 4 ,6], and we lookup 3
    # l[m] = 2, l[m+1] = 4, we will lookup in [1, 2],
    #    eventually returns (index of) 2
    # Suppose l = [1, 2, 4, 6], and we lookup 7, return (index of 6)
    # Suppose l = [1, 2, 4, 6], and we lookup 0, return (index of 1)
    if elt < l[i]:
        return 0
    else:
        return i + 1

def my_bisect_right(l, elt):
    assert l
    i = 0
    j = len(l) - 1
    return binary_search(l, elt, i, j)

assert bisect.bisect_right(l, 4) == my_bisect_right(l, 4)
assert bisect.bisect_right(l, 8) == my_bisect_right(l, 8)
assert bisect.bisect_right(l, 0) == my_bisect_right(l, 0)
assert bisect.bisect_right(l, 1) == my_bisect_right(l, 1)

# Application

#  biggest index in [i, j) such that tab[index] <= x
#    max((k for k, v in enumerate(tab[i:j]) if v <= x), default=None)

def f(tab, x, i, j):
    k = bisect.bisect_right(tab, x, i, j)
    return k - 1 if k else None


# A generic binary search
# return the first element  in [i:j+1] such that pred is True
# return j+1 if no such element exists
def binary_search(l, i, j, pred):
    assert i <= j
    while i < j:
        m = (i + j) // 2
        if pred(l[m]):
            j = m
        else:
            i = m + 1
    return i if pred(l[i]) else i + 1

def my_bisect_left(l, v):
    return binary_search(l, 0, len(l) - 1, lambda x: x >= v)

def my_bisect_right(l, v):
    return binary_search(l, 0, len(l) - 1, lambda x: x > v)

def bisect_find(l, v):
    i = binary_search(l, 0, len(l) - 1, lambda x : x >=v)
    return i < len(l) and l[i] == v

assert bisect.bisect_left(l, 4) == my_bisect_left(l, 4)
assert bisect.bisect_left(l, 8) == my_bisect_left(l, 8)
assert bisect.bisect_left(l, 0) == my_bisect_left(l, 0)
assert bisect.bisect_left(l, 1) == my_bisect_left(l, 1)
assert bisect.bisect_right(l, 4) == my_bisect_right(l, 4)
assert bisect.bisect_right(l, 8) == my_bisect_right(l, 8)
assert bisect.bisect_right(l, 0) == my_bisect_right(l, 0)
assert bisect.bisect_right(l, 1) == my_bisect_right(l, 1)

assert bisect_find(l, 1)
assert bisect_find(l, 4)
assert not bisect_find(l, 10)


# THE BINARY SEARCH, doesn't assume an array
#
# A generic binary search
# return the first element  in [i,j] such that pred is True
# return j+1 if no such element exists
def binary_search(i, j, pred):
    while i < j:
        m = (i + j) // 2
        assert i <= m < m + 1 <= j
        # mental model: [i,m] larger by at most one of [m+1,j]
        # each part is stricly smaller than [i, j]
        # no risk of infinite loop here, as long as we stop the loop
        # when i == j
        # - - - + + +
        # - - - - + +
        if pred(m):
            j = m
        else:
            i = m + 1
    return i if pred(i) else i + 1
