# TAGS tricky, many corner cases, stream
# see 5, 680
#
# @lc app=leetcode id=487 lang=python3
#
# [487] Max Consecutive Ones II
#
# https://leetcode.com/problems/max-consecutive-ones-ii/description/
#
# algorithms
# Medium (47.22%)
# Likes:    407
# Dislikes: 6
# Total Accepted:    27.9K
# Total Submissions: 59K
# Testcase Example:  '[1,0,1,1,0,1]'
#
#
# Given a binary array, find the maximum number of consecutive 1s in this array
# if you can flip at most one 0.
#
#
# Example 1:
#
# Input: [1,0,1,1,0]
# Output: 4
# Explanation: Flip the first zero will get the the maximum number of
# consecutive 1s.
# ⁠   After flipping, the maximum number of consecutive 1s is 4.
#
#
#
# Note:
#
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
#
#
#
# Follow up:
# What if the input numbers come in one by one as an infinite stream? In other
# words, you can't store all numbers coming from the stream as it's too large
# to hold in memory. Could you solve it efficiently?
#

# 0, 1, 0, 0, 0


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        # previous and current length of consecutive 1
        pre, cur, res = 0, 0, 0
        extra = False
        for n in nums:
            if n == 1:
                cur += 1
                if pre:
                    res = max(res, 1 + cur + pre)
                elif extra:
                    res = max(res, cur + 1)
                else:
                    res = max(res, cur)
            else:
                extra = True
                pre = cur
                cur = 0


        return res

