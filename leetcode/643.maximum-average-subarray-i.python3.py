def f(nums, k):
    cur_sum = sum(nums[i] for i in range(k))
    best = cur_sum
    for i in range(k, len(nums)):
        cur_sum = cur_sum + nums[i] - nums[i - k]
        best = max(best, cur_sum)
    return best / k


class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        return f(nums, k)
