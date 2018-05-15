#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (54.87%)
# Likes:    3038
# Dislikes: 72
# Total Accepted:    500.4K
# Total Submissions: 856.2K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
#
#
# TAGS backtrack, recursive

# @lc code=start

class Solution:

    # def subsets(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     n = len(nums)
    #     def f(i):
    #         if i == n:
    #             return [[]]
    #         a = nums[i]
    #         res = f(i+1)
    #         res.extend([[a] + i for i in res])
    #         return res
    #     return f(0)


    def subsets(self, nums):
            res = []
            n = len(nums)
            path = []
            def add(i):
                if i == n:
                    res.append(path.copy())
                else:
                    path.append(nums[i])
                    add(i+1)
                    path.pop()
                    add(i+1)
            add(0)
            return res

# @lc code=end

