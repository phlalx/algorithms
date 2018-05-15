#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (46.50%)
# Likes:    4993
# Dislikes: 524
# Total Accepted:    560.2K
# Total Submissions: 1.1M
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#
#
#
#
#
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In
# this case, the max area of water (blue section) the container can contain is
# 49.
#
#
#
# Example:
#
#
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
#

# My first idea was a monotonic stack, doesnt work because a container
# can extend beyond a wall.
#
# Tried: scanning, divide and conquer, monotonic stack
# Trick -> double pointer
#
# Very cool exercise.
#
# It can be seen as dp as well
#
# f(i, j) = max ( (j - i + 1) * min(height[i], height[j]), f(i+1, j), f(i, j-1))
#    the trick is that we only need to explore f(i+1, j) or f(i, j-1)
#   
#
# Scanning works but is suboptimal:
# f(i) = best answer for subarray [i:]
# f(i) = max(f(i+1), all area starting from i)
#
# Alternative: f(i) = best answer for subarray [:i+1], if we want to scan
#    from left to right
#
# f(i, j) = best answer for subarray [i:j+1]
#  the trick is to notice that if height[i] < height[j]
#    the best solution starting from i is necessarily [i:j+1] since
#     height[i] is the limiting height.
#
# Take-away: if no scanning solution, consider f(i, j) subproblems.
#

# @lc code=start
# TAGS: array, double pointer

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n - 1
        best = 0
        while i < j:
            best = max(best, (j - i) * min(height[j], height[i]))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return best

# @lc code=end

