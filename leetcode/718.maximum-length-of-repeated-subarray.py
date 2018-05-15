#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (47.19%)
# Likes:    946
# Dislikes: 40
# Total Accepted:    50.4K
# Total Submissions: 103.8K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# Given two integer arrays A and B, return the maximum length of an subarray
# that appears in both arrays.
#
# Example 1:
#
#
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation:
# The repeated subarray with maximum length is [3, 2, 1].
#
#
#
#
# Note:
#
#
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
#
#
#
#
#

# @lc code=start

# TAGS dp
# simple dp, some thing as longest common string 
# memo[i][j] = best solution starting on (i, j)
# TLE
#
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        p = len(B)
        memo = [[ None for _ in range(p+1)] for _ in range(n+1)]
        best = 0
        for i in reversed(range(n+1)):
            for j in reversed(range(p+1)):
                if i == n or j == p:
                    res = 0
                elif A[i] == B[j]:
                    res = 1 + memo[i+1][j+1]
                else:
                    res = 0
                memo[i][j] = res
                best = max(best, res)
        return best


# @lc code=end

