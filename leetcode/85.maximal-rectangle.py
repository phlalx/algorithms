#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#
# https://leetcode.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (34.44%)
# Likes:    2112
# Dislikes: 57
# Total Accepted:    152.8K
# Total Submissions: 426K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
# containing only 1's and return its area.
#
# Example:
#
#
# Input:
# [
# ⁠ ["1","0","1","0","0"],
# ⁠ ["1","0","1","1","1"],
# ⁠ ["1","1","1","1","1"],
# ⁠ ["1","0","0","1","0"]
# ]
# Output: 6
#
#
#

# @lc code=start
# TAGS classic, reduce to rectangle under histogram (monotonic stack)

def largestRectangleArea(heights):
    st = [-1]
    best = 0
    heights.append(0)
    for j, v in enumerate(heights):
        while st and heights[st[-1]] > v:
            height = heights[st.pop()]
            i = st[-1]
            best = max(best, (j - i - 1) * height)
        st.append(j)
    return best

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix)
        p = len(matrix[0])

        # preparing the matrix to reduce the problem to the histogram
        # problem
        histogram = [ [ None for _ in range(p) ] for _ in range(n) ]
        for j in range(p):
            height = None
            for i in range(n):
                if matrix[i][j] == '1':
                    if height is None:
                        height = i
                else:
                    height = None
                histogram[i][j] = 0 if height is None else i - height + 1

        res = 0
        for i in range(n):
            res = max(res, largestRectangleArea(histogram[i]))
        return res

# @lc code=end

