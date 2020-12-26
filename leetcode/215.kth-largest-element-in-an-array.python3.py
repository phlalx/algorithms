# TAGS array, heap, quickselect
# TODO worst-case linear time

#  https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/
#  https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/

import heapq

# inclusive bounds
def pivot(t, a, b):
    i = a + 1
    j = b
    p = t[a]
    while i <= j:
        if t[i] <= p:
            i += 1
        elif t[j] > p:
            j -= 1
        else:
            t[i], t[j] = t[j], t[i]
    t[i-1], t[a] = t[a], t[i-1]
    return i - 1


def test():
    nums = [3, 1, 1, 3, 4, 5, 6]
    res = pivot(nums, 0, len(nums) - 1)
    assert nums == [1, 1, 3, 3, 5, 6, 4]
    assert res == 3

# def quickselect(t, a, b, k):
#     kk = pivot(t, a, b)
#     pos = a + k
#     if pos == kk:
#         return t[kk]
#     elif pos < kk:
#         return kselect(t, a, kk-1, k)
#     else:
#         return kselect(t, kk+1, b, pos - kk - 1)

def quickselect(nums, k):

    i = 0
    j = len(nums) - 1

    while True:
        assert i <= k <= j
        i_p = pivot(nums, i, j)
        if i_p == k:
            return nums[i_p]
        elif k < i_p:
            j = i_p - 1
        else:
            i = i_p + 1


def sol_heap(nums, k):
    assert nums
    heapq.heapify(nums)
    for _ in range(k + 1):
        res = heapq.heappop(nums)
    return res


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # return sol_heap(nums, len(nums) - k)
        return quickselect(nums, len(nums) - k)
