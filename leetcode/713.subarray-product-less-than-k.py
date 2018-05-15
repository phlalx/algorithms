#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#
# https://leetcode.com/problems/subarray-product-less-than-k/description/
#
# algorithms
# Medium (37.41%)
# Likes:    796
# Dislikes: 41
# Total Accepted:    39K
# Total Submissions: 103.5K
# Testcase Example:  '[10,5,2,6]\n100'
#
# Your are given an array of positive integers nums.
# Count and print the number of (contiguous) subarrays where the product of all
# the elements in the subarray is less than k.
#
# Example 1:
#
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are: [10], [5],
# [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly
# less than k.
#
#
#
# Note:
# 0 < nums.length .
# 0 < nums[i] < 1000.
# 0 .
#
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, v: List[int], k: int) -> int:
        res = 0
        j = 0
        prod = 1
        n = len(v)
        for i in range(n):
            prod *= v[i]
            while j < i and prod >= k:
                prod /= v[j]
                j += 1
            if prod < k:
                res += i - j + 1
        return res

# @lc code=end

