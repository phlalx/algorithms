# TAGS dp, LIS


class Solution:
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []

        n = len(nums)
        nums.sort()
        memo = [None] * n

        def f(i):
            if memo[i] is not None:
                return memo[i]
            res = 1
            for j in range(i + 1, n):
                if nums[j] % nums[i] == 0:
                    res = max(res, 1 + f(j))
            memo[i] = res
            return res

        # TODO CHANGE THIS
        _m, i = max((f(i), i) for i in range(n))
        res = []

        def g(i):
            res.append(nums[i])
            for j in range(i + 1, n):
                if nums[j] % nums[i] == 0 and 1 + memo[j] == memo[i]:
                    g(j)
                    break

        g(i)

        return res
