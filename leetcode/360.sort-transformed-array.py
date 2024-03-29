#
# @lc app=leetcode id=360 lang=python3
#
# [360] Sort Transformed Array
#
# https://leetcode.com/problems/sort-transformed-array/description/
#
# algorithms
# Medium (47.27%)
# Likes:    242
# Dislikes: 70
# Total Accepted:    29.1K
# Total Submissions: 61.5K
# Testcase Example:  '[-4,-2,2,4]\n1\n3\n5'
#
# Given a sorted array of integers nums and integer values a, b and c. Apply a
# quadratic function of the form f(x) = ax^2 + bx + c to each element x in the
# array.
# 
# The returned array must be in sorted order.
# 
# Expected time complexity: O(n)
# 
# 
# Example 1:
# 
# 
# Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
# Output: [3,9,15,33]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
# Output: [-23,-5,1,7]
# 
# 
# 
#
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        res = [ a * x ^ 2 + b * x + c for x in nums]
        i = 0
        while i + 1 < n and res[i] <= res[i+1]:
            i += 1
        # res is sorted on [:i]
        # and reversed sorted on [i+1:]
        

