#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#
# https://leetcode.com/problems/transpose-matrix/description/
#
# algorithms
# Easy (63.91%)
# Likes:    290
# Dislikes: 263
# Total Accepted:    61.8K
# Total Submissions: 97K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix A, return the transpose of A.
# 
# The transpose of a matrix is the matrix flipped over it's main diagonal,
# switching the row and column indices of the matrix.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# 
# 
# 
# Example 2:
# 
# 
# Input: [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 1000
# 1 <= A[0].length <= 1000
# 
# 
# 
#

# @lc code=start
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        n = len(A)
        p = len(A[0])
        nn = p
        pp = n
        res = [ [ None for j in range(pp) ] for i in range(nn) ]
        for i in range(nn):
            for j in range(pp):
                res[i][j] = A[j][i]
        return res
        
# @lc code=end

