#
# @lc app=leetcode id=491 lang=python3
#
# [491] Increasing Subsequences
#
# https://leetcode.com/problems/increasing-subsequences/description/
#
# algorithms
# Medium (42.82%)
# Likes:    575
# Dislikes: 100
# Total Accepted:    40.3K
# Total Submissions: 91.7K
# Testcase Example:  '[4,6,7,7]'
#
# Given an integer array, your task is to find all the different possible
# increasing subsequences of the given array, and the length of an increasing
# subsequence should be at least 2.
# 
# 
# 
# Example:
# 
# 
# Input: [4, 6, 7, 7]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7],
# [4,7,7]]
# 
# 
# 
# 
# Note:
# 
# 
# The length of the given array will not exceed 15.
# The range of integer in the given array is [-100,100].
# The given array may contain duplicates, and two equal integers should also be
# considered as a special case of increasing sequence.
# 
# 
#
#TAGS recursive
# First idea was recursive, but it just a simple loop

# @lc code=start
# class Solution:
#     def findSubsequences(self, nums: List[int]) -> List[List[int]]:
#         def f(i):
#             if i == 0:
#                 return set()
#             else:
#                 res = set()
#                 res_before = f(i-1)
#                 res.update(res_before)
#                 v = nums[i-1]
#                 res_before.update((nums[j],) for j in range(i-1) if nums[j] <= v)
#                 res.update( u + (v,) for u in res_before if u[-1] <= v)
#             return res

#         res = f(len(nums))
#         return list(res)

class Solution:
    # trick count sequence with len < 2 and filter later
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = { () }
        for v in nums:
            res.update([u + (v,) for u in res if not u or u[-1] <= v])
        return [ u for u in res if len(u) >= 2 ]



# @lc code=end

