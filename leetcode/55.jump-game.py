#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (32.53%)
# Likes:    2589
# Dislikes: 249
# Total Accepted:    325.5K
# Total Submissions: 992.4K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
#
# Each element in the array represents your maximum jump length at that
# position.
#
# Determine if you are able to reach the last index.
#
# Example 1:
#
#
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its
# maximum
# jump length is 0, which makes it impossible to reach the last index.
#
#
#

# @lc code=start
#class Solution:
#    def canJump(self, nums: List[int]) -> bool:
#        n = len(nums)
#        memo = {}
#        def f(i):
#            if i >= n-1:
#                return True
#            elif nums[i] == 0:
#                return False
#            if i in memo:
#                return memo[i]
#            res = any(f(i + k) for k in range(1, nums[i]+1))
#            memo[i] = res
#            return res
#        for i in reversed(range(n)):
#            f(i)
#        return f(0)

#TAGS greedy
# dp (n^2) is TLE. There is a simple linear solution. 
# Scan the array backward and memorize the smaller index that allows us
# to reach the end.
# 

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        smaller = len(nums) - 1
        for i in reversed(range(len(nums))):
            v = nums[i]
            if i + v >= smaller:
                smaller = i
        return smaller == 0

# @lc code=end

