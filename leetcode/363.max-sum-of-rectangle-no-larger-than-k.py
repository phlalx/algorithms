#
# @lc app=leetcode id=363 lang=python3
#
# [363] Max Sum of Rectangle No Larger Than K
#
# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/description/
#
# algorithms
# Hard (35.59%)
# Likes:    631
# Dislikes: 42
# Total Accepted:    36.7K
# Total Submissions: 100.9K
# Testcase Example:  '[[1,0,1],[0,-2,3]]\n2'
#
# Given a non-empty 2D matrix matrix and an integer k, find the max sum of a
# rectangle in the matrix such that its sum is no larger than k.
#
# Example:
#
#
# Input: matrix = [[1,0,1],[0,-2,3]], k = 2
# Output: 2
# Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is
# 2,
# and 2 is the max number no larger than k (k = 2).
#
# Note:
#
#
# The rectangle inside the matrix must have an area > 0.
# What if the number of rows is much larger than the number of columns?
#
#
# Idea:
#  Reduce to (variant of) kadane
#
#  Reminder: Kadane = find subarray with larger sum
#
# First, we select the border lines of the rectangles O(n^2)
# Then we compute the sum for each column (using prefix sum, O(p))
# Last step is to find the largest sum larger than K
#
# The last step could be a hard problem on its own
#
# Find the larget sum no larger than K of a subarray
#
# See 1074 (same problem with different 1-D problem)

# @lc code=start
import bisect

def ksum(nums, k):
    best = float('-inf')
    seen = [0]
    acc = 0
    for v in nums:
        acc += v
        i = bisect.bisect_left(seen, acc - k)
        if i < len(seen):
            best = max(best, acc - seen[i])
        bisect.insort(seen, acc)
    return best

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix)
        p = len(matrix[0])
        ps_matrix = [[ 0 for j in range(p)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(p):
                ps_matrix[i][j] = ps_matrix[i-1][j] + matrix[i-1][j]
        best = float('-inf')
        for i in range(n):
            for ii in range(i,n):
                tmp = [ps_matrix[ii+1][j] - ps_matrix[i][j] for j in range(p)]
                best = max(best, ksum(tmp, k))
        return best

# @lc code=end

