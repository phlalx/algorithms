#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (34.11%)
# Likes:    1568
# Dislikes: 234
# Total Accepted:    282.8K
# Total Submissions: 828.6K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?
# 
# 
# 
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 
# Note: m and n will be at most 100.
# 
# Example 1:
# 
# 
# Input:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# 
# 
#

# @lc code=start
#TAGS simple dp

import functools

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        n = len(obstacleGrid)
        p = len(obstacleGrid[0])

        def reachable(i, j):
            if i + 1 < n and not obstacleGrid[i+1][j]:
                yield (i+1, j)
            if j + 1 < p and not obstacleGrid[i][j+1]:
                yield (i, j+1)

        @functools.lru_cache
        def f(i, j):
            if i == n - 1 and j == p - 1:
                return int(obstacleGrid[i][j] == 0)
            return sum(f(ii, jj) for ii, jj in reachable(i, j))
            
        return f(0, 0)
        
# @lc code=end

