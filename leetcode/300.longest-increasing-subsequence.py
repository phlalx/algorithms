#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (41.35%)
# Likes:    3692
# Dislikes: 83
# Total Accepted:    314.1K
# Total Submissions: 749.4K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
#
# Example:
#
#
# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4.
#
# Note:
#
#
# There may be more than one LIS combination, it is only necessary for you to
# return the length.
# Your algorithm should run in O(n^2) complexity.
#
#
# Follow up: Could you improve it to O(n log n) time complexity?
#
#
# @lc code=start
# TAGS array, classic

import bisect

# A generic binary search
# return the first element  in [i:j+1] such that pred is True
# return j+1 if no such element exists
def binary_search(l, i, j, pred):
    assert i <= j
    while i < j:
        m = (i + j) // 2
        if pred(l[m]):
            j = m
        else:
            i = m + 1
    return i if pred(l[i]) else i + 1

def patience(nums):
    n = len(nums)
    # best[i] = index of last element of subsequence of length (i + 1)
    best = [0]
    for i in range(1, n):
        height = nums[i]
        # returns the index of the first value greater than heigth
        # in best[:best]
        pred = lambda i: nums[i] >= height
        j = binary_search(best, 0, len(best) - 1, pred)
        if j == len(best):
            best.append(i)
        else:
            best[j] = i
    return len(best)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums:
            return patience(nums)
        else:
            return 0

# @lc code=end

