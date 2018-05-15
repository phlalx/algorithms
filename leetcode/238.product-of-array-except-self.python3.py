# TAGS array
# TODO to slow


class Solution:
    def productExceptSelf(self, nums):
        """ 
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        assert n >= 1

        res = [None] * n
        arr2 = [1] * n  # arr2[i] = prod of num[j] for j > i
        for i in range(1, n):
            arr2[n - i - 1] = arr2[n - i] * nums[n - i]
        cur_prod = 1
        for i, v in enumerate(nums):
            res[i] = cur_prod * arr2[i]
            cur_prod = cur_prod * v
        return res
