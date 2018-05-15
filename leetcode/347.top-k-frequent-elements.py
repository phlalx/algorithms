
import heapq


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

class Solution:
    def topKFrequent(self, nums, k):
       kselect(nums, k)
       return nums[0:k]
