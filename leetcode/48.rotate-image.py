# TAGS implem
# make a drawing
#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
# https://leetcode.com/problems/rotate-image/description/
#
# algorithms
# Medium (50.40%)
# Likes:    2053
# Dislikes: 179
# Total Accepted:    307.7K
# Total Submissions: 596.5K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# Note:
#
# You have to rotate the image in-place, which means you have to modify the
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the
# rotation.
#
# Example 1:
#
#
# Given input matrix =
# [
# ⁠ [1,2,3],
# ⁠ [4,5,6],
# ⁠ [7,8,9]
# ],
#
# rotate the input matrix in-place such that it becomes:
# [
# ⁠ [7,4,1],
# ⁠ [8,5,2],
# ⁠ [9,6,3]
# ]
#
#
# Example 2:
#
#
# Given input matrix =
# [
# ⁠ [ 5, 1, 9,11],
# ⁠ [ 2, 4, 8,10],
# ⁠ [13, 3, 6, 7],
# ⁠ [15,14,12,16]
# ],
#
# rotate the input matrix in-place such that it becomes:
# [
# ⁠ [15,13, 2, 5],
# ⁠ [14, 3, 4, 1],
# ⁠ [12, 6, 8, 9],
# ⁠ [16, 7,10,11]
# ]
#
#
#

# @lc code=start
class Solution:
    def rotate(self, t: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not t or not t[0]:
            return t
        n = len(t[0])
        for a in range(n // 2):
            b = n - a - 1
            for i in range(b - a):
                t[a][a+i], t[a+i][b], t[b][b-i], t[b-i][a] = t[b-i][a], t[a][a+i], t[a+i][b], t[b][b-i]


# @lc code=end

