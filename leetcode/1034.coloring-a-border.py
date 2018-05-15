#
# @lc app=leetcode id=1034 lang=python3
#
# [1034] Coloring A Border
#
# https://leetcode.com/problems/coloring-a-border/description/
#
# algorithms
# Medium (42.64%)
# Likes:    81
# Dislikes: 196
# Total Accepted:    7.9K
# Total Submissions: 18K
# Testcase Example:  '[[1,1],[1,2]]\n0\n0\n3'
#
# Given a 2-dimensional grid of integers, each value in the grid represents the
# color of the grid square at that location.
#
# Two squares belong to the same connected component if and only if they have
# the same color and are next to each other in any of the 4 directions.
#
# The border of a connected component is all the squares in the connected
# component that are either 4-directionally adjacent to a square not in the
# component, or on the boundary of the grid (the first or last row or column).
#
# Given a square at location (r0, c0) in the grid and a color, color the border
# of the connected component of that square with the given color, and return
# the final grid.
#
#
#
# Example 1:
#
#
# Input: grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3
# Output: [[3, 3], [3, 2]]
#
#
#
# Example 2:
#
#
# Input: grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3
# Output: [[1, 3, 3], [2, 3, 3]]
#
#
#
# Example 3:
#
#
# Input: grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2
# Output: [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
#
#
#
#
#
# Note:
#
#
# 1 <= grid.length <= 50
# 1 <= grid[0].length <= 50
# 1 <= grid[i][j] <= 1000
# 0 <= r0 < grid.length
# 0 <= c0 < grid[0].length
# 1 <= color <= 1000
#
#
#TAGS dfs graph
# simple problem
# @lc code=start

class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        visited = set()
        border = []

        component_color = grid[r0][c0]
        if component_color == 0:
            return grid

        n = len(grid)
        p = len(grid[0])

        def neigh(s):
            i, j = s
            for di, dj in zip([0,1,0,-1], [1,0,-1,0]):
                ii = i + di
                jj = j + dj
                if 0 <= ii < n and 0 <= jj < p and grid[ii][jj] == component_color:
                    yield ii, jj

        def is_border(s):
            i, j = s
            for di, dj in zip([0,1,0,-1], [1,0,-1,0]):
                ii = i + di
                jj = j + dj
                if not (0 <= ii < n and 0 <= jj < p):
                    return True
                if grid[ii][jj] == 0:
                    return True
                if grid[ii][jj] != component_color:
                    return True
            return False

        def dfs(s):
            if is_border(s):
                border.append(s)
            for ss in neigh(s):
                if ss not in visited:
                    visited.add(ss)
                    dfs(ss)

        dfs((r0, c0))

        for i, j in border:
            grid[i][j] = color

        return grid

# @lc code=end

