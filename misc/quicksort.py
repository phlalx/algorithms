

# Loop invariant
#
#      [ x <= p | p | ...  | y > p ]
#                 i      j
#
# True at the beginning
# And we stop when i == j


def pivot(t, i, j):
    p = t[i]
    while i < j:
        x = t[i+1]
        if x <= p:
            t[i+1], t[i] = t[i], t[i+1]
            i += 1
        else:
            t[i+1], t[j] = t[j], t[i+1]
            j -= 1
    assert t[i] == p
    return i

def quicksort_aux(t, i, j):
    if i < j:
        p = pivot(t, i, j)
        assert i <= p <= j
        quicksort_aux(t, i, p-1)
        quicksort_aux(t, p+1, j)

def quicksort(t):
    quicksort_aux(t, 0, len(t) - 1)

def test(t):
    res = sorted(t)
    quicksort(t)
    assert t == res

test([])
test([1])
test([1, 2, 3])
test([3, 2, 1])
test([3, 3, 1])
test([5, 1, 2, 3])
test([3, 6, 2, 1])
test([3, 3, 7, 1])
