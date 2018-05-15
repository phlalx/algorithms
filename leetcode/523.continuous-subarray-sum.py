#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#
# https://leetcode.com/problems/continuous-subarray-sum/description/
#
# algorithms
# Medium (24.24%)
# Likes:    1107
# Dislikes: 1559
# Total Accepted:    110K
# Total Submissions: 449.6K
# Testcase Example:  '[23,2,4,6,7]\n6'
#
# Given a list of non-negative numbers and a target integer k, write a function
# to check if the array has a continuous subarray of size at least 2 that sums
# up to a multiple of k, that is, sums up to n*k where n is also an
# integer.
#
#
#
# Example 1:
#
#
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to
# 6.
#
#
# Example 2:
#
#
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and
# sums up to 42.
#
#
#
#
# Note:
#
#
# The length of the array won't exceed 10,000.
# You may assume the sum of all the numbers is in the range of a signed 32-bit
# integer.
#
#
#

# @lc code=start
#TAGS variant on 2-sum
#
# Several tricks
#   1. reduce to two-sum with partial sums and mod k
#   2. corner case % k
#   3. sub array length >= 2, imply to maintain cur and cur_prev
#   see 974 for a simpler variant

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prev = {0}
        cur_prev = 0
        cur = nums[0] % k if k else nums[0]
        for i in range(1, n):
            tmp = cur + nums[i]
            cur_prev, cur = cur, (tmp % k if k else tmp)
            if cur in prev:
                return True
            prev.add(cur_prev)
        return False


# @lc code=end

