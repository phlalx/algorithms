# TAGS  dp, cool
#  for thing to note -> it's a variation on kadane
#
#
#
# @lc app=leetcode id=1186 lang=python3
#
# [1186] Maximum Subarray Sum with One Deletion
#
# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/description/
#
# algorithms
# Medium (25.75%)
# Likes:    202
# Dislikes: 9
# Total Accepted:    6.2K
# Total Submissions: 18.7K
# Testcase Example:  '[1,-2,0,3]'
#
# Given an array of integers, return the maximum sum for a non-empty subarray
# (contiguous elements) with at most one element deletion. In other words, you
# want to choose a subarray and optionally delete one element from it so that
# there is still at least one element left and the sum of the remaining
# elements is maximum possible.
#
# Note that the subarray needs to be non-empty after deleting one element.
#
#
# Example 1:
#
#
# Input: arr = [1,-2,0,3]
# Output: 4
# Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the
# subarray [1, 0, 3] becomes the maximum value.
#
# Example 2:
#
#
# Input: arr = [1,-2,-2,3]
# Output: 3
# Explanation: We just choose [3] and it's the maximum sum.
#
#
# Example 3:
#
#
# Input: arr = [-1,-1,-1,-1]
# Output: -1
# Explanation: The final subarray needs to be non-empty. You can't choose [-1]
# and delete -1 from it, then get an empty subarray to make the sum equals to
# 0.
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 10^5
# -10^4 <= arr[i] <= 10^4
#
#

# @lc code=start
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        cur_0 = float('-inf')
        cur_1 = float('-inf')
        res = float('-inf')
        for v in arr:
            # Careful, simultaneous change
            cur_0, cur_1 = v + max(0, cur_0), max(cur_0, v + cur_1)
            res = max(res, cur_0, cur_1)
        return res

# @lc code=end

