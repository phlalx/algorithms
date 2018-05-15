#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
#
# algorithms
# Medium (43.36%)
# Likes:    1299
# Dislikes: 72
# Total Accepted:    67.5K
# Total Submissions: 151.9K
# Testcase Example:  '[4,3,2,3,5,2,1]\n4'
#
# Given an array of integers nums and a positive integer k, find whether it's
# possible to divide this array into k non-empty subsets whose sums are all
# equal.
#
#
#
# Example 1:
#
#
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3),
# (2,3) with equal sums.
#
#
#
#
# Note:
#
#
# 1 <= k <= len(nums) <= 16.
# 0 < nums[i] < 10000.
#
#
#

# @lc code=start

#TAGS dp, cool
# generalization of 473, 1013
# TODO too slow, try dfs or dp with bitmask

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        nums.sort(reverse=True)
        l, r = divmod(sum(nums), k)
        if r != 0:
            return False
        n = len(nums)
        memo = {}
        def f(i, x):
            res = memo.get((i, x))
            if res is not None:
                return res
            if i == n:
                res = all(y == l for y in x)
            else:
                res = False
                for j in range(k):
                    if x[j] + nums[i] <= l:
                        xx = list(x)
                        xx[j] += + nums[i]
                        if f(i+1, tuple(xx)):
                            res = True
                            break
            memo[(i, x)] = res
            return res
        return f(0, (0,) * k)

# use backtrack
# take away: if you need to carry a big state in the dp solution (or/and
#            if you want to display the solutions)
#            think backtrack
#

class Solution:
    def canPartitionKSubsets(self, nums, k):
        l, r = divmod(sum(nums), k)
        if r != 0:
            return False
        n = len(nums)
        nums.sort(reverse=True)
        # we can reach False sooner if we start placing the big values
        bucket = [0] * k
        def f(i):
            if i == n:
                return max(bucket) == l
            v = nums[i]
            for j in range(k):
                if bucket[j] + v <= l:
                    bucket[j] += v
                    if f(i+1):
                        return True
                    bucket[j] -= v
                    if bucket[j] == 0:  # trick1
                        return False  # this restrict the states we explore
                        # to [ XXXXX, 0, 0 ] (taking adv. of symmetry)
            return False
        return f(0)
# @lc code=end

