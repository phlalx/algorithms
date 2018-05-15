#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#
# https://leetcode.com/problems/01-matrix/description/
#
# algorithms
# Medium (36.68%)
# Likes:    804
# Dislikes: 82
# Total Accepted:    52.3K
# Total Submissions: 142.7K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for
# each cell.
#
# The distance between two adjacent cells is 1.
#
#
#
# Example 1:
#
#
# Input:
# [[0,0,0],
# ⁠[0,1,0],
# ⁠[0,0,0]]
#
# Output:
# [[0,0,0],
# [0,1,0],
# [0,0,0]]
#
#
# Example 2:
#
#
# Input:
# [[0,0,0],
# ⁠[0,1,0],
# ⁠[1,1,1]]
#
# Output:
# [[0,0,0],
# ⁠[0,1,0],
# ⁠[1,2,1]]
#
#
#
#
# Note:
#
#
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.
#
#
#
#TAGS multisource BFS, see 286

# @lc code=start
# This is too slow, quite similar to Bellman-Ford

# class Solution:
#   def updateMatrix(self, matrix):
#     if not matrix or not matrix[0]:
#       return matrix
#     n = len(matrix)
#     p = len(matrix[0])

#     def neighbors(i, j):
#       u = [0, 1, 0, -1]
#       v = [1, 0, -1, 0]
#       for a, b in zip(u, v):
#         ii = i + a
#         jj = j + b
#         if 0 <= ii < n and 0 <= jj < p:
#           yield ii, jj

#     k = n + p
#     for _ in range(k):
#       for i in range(n):
#         for j in range(p):
#           if matrix[i][j] != 0:
#             matrix[i][j] = min(1 + matrix[ii][jj] for ii, jj in neighbors(i, j))
#     return matrix

from collections import deque

class Solution:
  def updateMatrix(self, matrix):
    if not matrix or not matrix[0]:
      return matrix
    n = len(matrix)
    p = len(matrix[0])

    def neighbors(i, j):
      u = [0, 1, 0, -1]
      v = [1, 0, -1, 0]
      for a, b in zip(u, v):
        ii = i + a
        jj = j + b
        if 0 <= ii < n and 0 <= jj < p:
          yield ii, jj

    q = deque()

    for i in range(n):
        for j in range(p):
            m = matrix[i][j]
            if m == 0:
                q.appendleft((i,j))
            else:
                matrix[i][j] = None

    while(q):
        i, j = q.pop()
        for ii, jj in neighbors(i, j):
            if matrix[ii][jj] is None:
                matrix[ii][jj] = matrix[i][j] + 1
                q.appendleft((ii, jj))

    return matrix


# @lc code=end

