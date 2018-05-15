#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (41.52%)
# Likes:    1885
# Dislikes: 54
# Total Accepted:    134.6K
# Total Submissions: 318.7K
# Testcase Example:  '[1,5,11,5]'
#
# Given a non-empty array containing only positive integers, find if the array
# can be partitioned into two subsets such that the sum of elements in both
# subsets is equal.
#
# Note:
#
#
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
#
#
#
#
# Example 1:
#
#
# Input: [1, 5, 11, 5]
#
# Output: true
#
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
#
#
#
# Example 2:
#
#
# Input: [1, 2, 3, 5]
#
# Output: false
#
# Explanation: The array cannot be partitioned into equal sum subsets.
#
#
#
#
#

# @lc code=start
#TAGS dp
# subset-sum, TODO can we make it faster
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        target = s // 2
        n = len(nums)
        memo = [[ None for _ in range(target+1)] for _ in range(n + 1) ]
        def f(i, s):
            res = memo[i][s]
            if res is not None:
                return res
            if i == n:
                res = s == 0
            else:
                res = f(i+1, s-nums[i]) or f(i+1, s)
            memo[i][s] = res
            return res
        return f(0, target)

# @lc code=end

