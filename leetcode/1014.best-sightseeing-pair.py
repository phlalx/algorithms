#
# @lc app=leetcode id=1014 lang=python3
#
# [1014] Best Sightseeing Pair
#
# https://leetcode.com/problems/best-sightseeing-pair/description/
#
# algorithms
# Medium (50.25%)
# Likes:    347
# Dislikes: 19
# Total Accepted:    13.3K
# Total Submissions: 25.7K
# Testcase Example:  '[8,1,5,2,6]'
#
# Given an array A of positive integers, A[i] represents the value of the i-th
# sightseeing spot, and two sightseeing spots i and j have distance j - i
# between them.
#
# The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) :
# the sum of the values of the sightseeing spots, minus the distance between
# them.
#
# Return the maximum score of a pair of sightseeing spots.
#
#
#
# Example 1:
#
#
# Input: [8,1,5,2,6]
# Output: 11
# Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
#
#
#
#
# Note:
#
#
# 2 <= A.length <= 50000
# 1 <= A[i] <= 1000
#
#

# @lc code=start
#TAGS array
# classic array scanning, and store element in the proper datastructure
# similar to buy/sell stock
# I made the stupid mistake of using a heap for keeping track of the
# largest element seen so far

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        largest_ai_plus_i = A[0]
        res = float('-inf')
        n = len(A)
        for j in range(1, n):
            res = max(res, A[j] - j + largest_ai_plus_i)
            largest_ai_plus_i = max(largest_ai_plus_i, A[j] + j)
        return res



# @lc code=end

