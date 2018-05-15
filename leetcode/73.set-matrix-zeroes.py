#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (40.74%)
# Likes:    1326
# Dislikes: 231
# Total Accepted:    243.1K
# Total Submissions: 591.7K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in-place.
#
# Example 1:
#
#
# Input:
# [
# [1,1,1],
# [1,0,1],
# [1,1,1]
# ]
# Output:
# [
# [1,0,1],
# [0,0,0],
# [1,0,1]
# ]
#
#
# Example 2:
#
#
# Input:
# [
# [0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]
# ]
# Output:
# [
# [0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]
# ]
#
#
# Follow up:
#
#
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
#
#
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        assert n and m

        erase_first_line = 0 in matrix[0]
        erase_first_col = 0 in (matrix[i][0] for i in range(n))

        for i in range(1, n):
            for j in range(1,  m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        def erase_line(i):
            for j in range(m):
                matrix[i][j] = 0

        def erase_col(j):
            for i in range(n):
                matrix[i][j] = 0

        for i in range(1, n):
            if matrix[i][0] == 0:
                erase_line(i)

        for j in range(m):
            if matrix[0][j] == 0:
                erase_col(j)

        if erase_first_col:
            erase_col(0)

        if erase_first_line:
            erase_line(0)

        return matrix

# @lc code=end

