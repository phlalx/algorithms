#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (40.62%)
# Likes:    1522
# Dislikes: 179
# Total Accepted:    216.3K
# Total Submissions: 516.2K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you
# may move to adjacent numbers on the row below.
#
# For example, given the following triangle
#
#
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
#
#
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
#
# Bonus point if you are able to do this using only O(n) extra space, where n
# is the total number of rows in the triangle.
#
#

#TAGS dp
#TODO iterative dp with space optimization

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        memo = {}
        def f(i, j):
            res = memo.get((i,j))
            if res is not None:
                return res
            if i == n:
                res = 0
            else:
                res = triangle[i][j] + min(f(i+1, j), f(i+1, j+1) )
            memo[i,j] = res
            return res
        return f(0, 0)
            


# @lc code=end

