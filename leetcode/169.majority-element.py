#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (53.98%)
# Likes:    2327
# Dislikes: 192
# Total Accepted:    487.5K
# Total Submissions: 879.4K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always
# exist in the array.
#
# Example 1:
#
#
# Input: [3,2,3]
# Output: 3
#
# Example 2:
#
#
# Input: [2,2,1,1,1,2,2]
# Output: 2
#
#
#
# TODO comprendre cet algo

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        best = None
        count = 0
        for n in nums:
            if count == 0:
                best = n
                count = 1
            elif n == best:
                count += 1
            else:
                count -= 1
        return best

# @lc code=end

