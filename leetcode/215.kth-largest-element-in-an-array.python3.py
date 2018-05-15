# TAGS array, heap, quickselect
# TODO worst-case linear time

#  https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/
#  https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/

import heapq

# inclusive bounds
def pivot(nums, i, j):
    p = nums[i]
    while i != j:
        assert nums[i] == p
        if nums[i + 1] <= p:
            nums[i], nums[i + 1] = nums[i + 1], p
            i += 1
        else:
            nums[j], nums[i + 1] = nums[i + 1], nums[j]
            j -= 1
    return i


def test():
    nums = [3, 1, 1, 3, 4, 5, 6]
    res = pivot(nums, 0, len(nums) - 1)
    assert nums == [1, 1, 3, 3, 5, 6, 4]
    assert res == 3


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
