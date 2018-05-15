# KSELECT
# things to remember
# first specify partition operation correctly, pick first element as pivot
# by default saves a few lines. Specify range of subarray with python
# convention. Return index of pivot.
#
# in kselect, partition returns an 'absolute' position in the array,
# but we need to compare it to an offset from starting point of considered
# array.

from random import randrange

# precondition:
# pivot index p_i in range(a, b)
# returns k such that a <= k < b and sorted(l[a:b])[k - a] = p
# side-effect: partition l such that l[a:k] <= p, l[k+1:b] > p, l[k] = p
#
# partition moves l[p_i] where it should be if the array was sorted
def partition(l, p_i, a, b):
    assert p_i in range(a, b)
    p = l[p_i]
    l[a], l[p_i] = l[p_i], l[a]
    i = a + 1
    j = b - 1
    while i <= j:
        if l[i] <= p:
            i += 1
        elif l[j] > p:
            j -= 1
        else:
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1
    i = i - 1
    l[i], l[a] = l[a], l[i]
    assert all(v <= p for v in l[a:i])
    assert all(v > p for v in l[i+1:b])
    assert l[i] == p
    assert a <= i < b
    return i

def partition_pivot_first(l, a, b):
    i = a + 1
    j = b - 1
    p = l[a]
    while i <= j:
        if l[i] <= p:
            i += 1
        elif l[j] > p:
            j -= 1
        else:
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1
    i = i - 1
    l[i], l[a] = l[a], l[i]
    return i

# precondition l is not empty, and k in range(l)
# return elements of rank k in list l
def kselect(l, k):
    assert l
    n = len(l)
    assert 0 <= k < n
    i = 0
    j = n
    while i < j:
        kk = partition_pivot_first(l, i, j)
        if k == kk:  # we are lucky, that's exactly the rank we were looking for
            return l[k]
        elif k < kk:
            j = kk  # lookup in first half
        else: # i + k > kk
            i = kk + 1 # lookup in second half, but adjust rank
    assert False

def quicksort(l, i, j):
    if j - i <= 1:
        return
    k = partition(l, i, i, j)
    quicksort(l, i, k)
    quicksort(l, k+1, j)

def test_quicksort(l):
    l2 = sorted(l)
    quicksort(l, 0, len(l))
    assert(l == l2)

def test_partition(l):
    n = len(l)
    a = randrange(0, n - 1)
    b = randrange(a + 1, n + 1)
    assert a < b
    p_i = randrange(a, b)
    p = l[p_i]
    j = partition(l, p_i, a, b)
    assert sorted(l[a:b])[j-a] == p

def test_kselect(l, i):
    assert kselect(l, i) == sorted(l)[i]

def main():
    for _ in range(1000):
        n = randrange(2, 100)
        l = [ randrange(-100, 100) for _ in range(n) ]
        k = randrange(n)
        test_kselect(list(l), k)
        test_quicksort(list(l))
        test_partition(list(l))

main()