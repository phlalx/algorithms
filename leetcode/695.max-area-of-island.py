#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#
# https://leetcode.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (58.62%)
# Likes:    1421
# Dislikes: 67
# Total Accepted:    115.2K
# Total Submissions: 192.1K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.) You
# may assume all four edges of the grid are surrounded by water.
#
# Find the maximum area of an island in the given 2D array. (If there is no
# island, the maximum area is 0.)
#
# Example 1:
#
#
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,1,1,0,1,0,0,0,0,0,0,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,0,1,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,1,1,0,0],
# ⁠[0,0,0,0,0,0,0,0,0,0,1,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,0,0,0,0]]
#
# Given the above grid, return 6. Note the answer is not 11, because the island
# must be connected 4-directionally.
#
# Example 2:
#
#
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
#
# Note: The length of each dimension in the given grid does not exceed 50.
#
#

#TAGS dfs

import itertools

# @lc code=start
class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        n = len(grid)
        p = len(grid[0])
        ingrid = lambda i, j: 0 <= i < n and 0 <= j < p
        def dfs(i, j):
            res = 1
            for a, b in zip([0,1,0,-1], [1,0,-1,0]):
                ii = i + a
                jj = j + b
                if ingrid(ii, jj) and grid[ii][jj] == 1:
                    grid[ii][jj] = -1
                    res += dfs(ii, jj)
            return res
        res = 0
        for i, j in itertools.product(range(n), range(p)):
            if grid[i][j] == 1:
                grid[i][j] = -1
                s = dfs(i, j)
                res = max(s, res)
        return res




# @lc code=end

