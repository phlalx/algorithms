#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (40.90%)
# Likes:    1612
# Dislikes: 32
# Total Accepted:    129.4K
# Total Submissions: 304.4K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# Given an integer matrix, find the length of the longest increasing path.
# 
# From each cell, you can either move to four directions: left, right, up or
# down. You may NOT move diagonally or move outside of the boundary (i.e.
# wrap-around is not allowed).
# 
# Example 1:
# 
# 
# Input: nums = 
# [
# ⁠ [9,9,4],
# ⁠ [6,6,8],
# ⁠ [2,1,1]
# ] 
# Output: 4 
# Explanation: The longest increasing path is [1, 2, 6, 9].
# 
# 
# Example 2:
# 
# 
# Input: nums = 
# [
# ⁠ [3,4,5],
# ⁠ [3,2,6],
# ⁠ [2,2,1]
# ] 
# Output: 4 
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally
# is not allowed.
# 
# 
#
#TAGS dp, dag

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        if not matrix or not matrix[0]:
            return 0

        n = len(matrix)
        p = len(matrix[0])

        def neigh(i, j):
            for di, dj in zip([0,1,0,-1], [1,0,-1,0]):
                ii = i + di
                jj = j + dj
                if 0 <= ii < n and 0 <= jj < p and matrix[i][j] < matrix[ii][jj]:
                    yield ii, jj

        memo = [[None for _i in range(p)] for _j in range(n)]

        def dfs_rec(i, j):
            res = memo[i][j]
            if res is not None:
                return res
            res = max((1 + dfs_rec(ii, jj) for ii, jj in neigh(i, j)), default=1)
            memo[i][j] = res
            return res

        return max(dfs_rec(i, j) for i in range(n) for j in range(p))
            
        
    # @lc code=end

