#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#
# https://leetcode.com/problems/reshape-the-matrix/description/
#
# algorithms
# Easy (59.29%)
# Likes:    669
# Dislikes: 94
# Total Accepted:    90.1K
# Total Submissions: 150.8K
# Testcase Example:  '[[1,2],[3,4]]\n1\n4'
#
# In MATLAB, there is a very useful function called 'reshape', which can
# reshape a matrix into a new one with different size but keep its original
# data.
# 
# 
# 
# You're given a matrix represented by a two-dimensional array, and two
# positive integers r and c representing the row number and column number of
# the wanted reshaped matrix, respectively.
# 
# ⁠The reshaped matrix need to be filled with all the elements of the original
# matrix in the same row-traversing order as they were.
# 
# 
# 
# If the 'reshape' operation with given parameters is possible and legal,
# output the new reshaped matrix; Otherwise, output the original matrix.
# 
# 
# Example 1:
# 
# Input: 
# nums = 
# [[1,2],
# ⁠[3,4]]
# r = 1, c = 4
# Output: 
# [[1,2,3,4]]
# Explanation:The row-traversing of nums is [1,2,3,4]. The new reshaped matrix
# is a 1 * 4 matrix, fill it row by row by using the previous list.
# 
# 
# 
# Example 2:
# 
# Input: 
# nums = 
# [[1,2],
# ⁠[3,4]]
# r = 2, c = 4
# Output: 
# [[1,2],
# ⁠[3,4]]
# Explanation:There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So
# output the original matrix.
# 
# 
# 
# Note:
# 
# The height and width of the given matrix is in range [1, 100].
# The given r and c are all positive.
# 
# 
#

# @lc code=start
class Solution:
    def matrixReshape(self, nums: List[List[int]], R: int, C: int) -> List[List[int]]:
        n = len(nums)
        p = len(nums[0])
        if n * p != R * C:
            return nums
        res = [ [ None for j in range(C)] for i in range(R)]
        r = 0
        c = 0
        for i in range(n):
            for j in range(p):
                res[r][c] = nums[i][j]
                c = c + 1
                if c == C:
                    c = 0
                    r = r + 1
        return res

        
# @lc code=end

