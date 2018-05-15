#
# @lc app=leetcode id=1074 lang=python3
#
# [1074] Number of Submatrices That Sum to Target
#
# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/description/
#
# algorithms
# Hard (59.32%)
# Likes:    469
# Dislikes: 24
# Total Accepted:    15K
# Total Submissions: 25.3K
# Testcase Example:  '[[0,1,0],[1,1,1],[0,1,0]]\n0'
#
# Given a matrix, and a target, return the number of non-empty submatrices that
# sum to target.
#
# A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x
# <= x2 and y1 <= y <= y2.
#
# Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if
# they have some coordinate that is different: for example, if x1 != x1'.
#
#
#
# Example 1:
#
#
# Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
# Output: 4
# Explanation: The four 1x1 submatrices that only contain 0.
#
#
#
# Example 2:
#
#
# Input: matrix = [[1,-1],[-1,1]], target = 0
# Output: 5
# Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the
# 2x2 submatrix.
#
#
#
#
#
# Note:
#
#
# 1 <= matrix.length <= 300
# 1 <= matrix[0].length <= 300
# -1000 <= matrix[i] <= 1000
# -10^8 <= target <= 10^8
#
#
#

# @lc code=start
# TAGS matrix, 2-sum
# See 363 (same problem with different 1-D problem)
# trick:
#
# fix i and ii, and reduce to a 1-dimensional problem
# O(p^2*n)
#
from collections import Counter

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix)
        p = len(matrix[0])
        m = [ [0] * (p+1) for _ in range(n) ]
        for i in range(n):
            for j in range(1, p+1):
                m[i][j] = m[i][j-1] + matrix[i][j-1]
        res = 0
        for j in range(p+1):
            for jj in range(j+1, p+1):
                f = lambda i : m[i][jj] - m[i][j]
                seen = Counter([0])
                cur = 0
                for i in range(n):
                    cur += f(i)
                    if cur - target in seen:
                        res += seen[cur - target]
                    seen[cur] += 1
        return res

# @lc code=end

