#
# @lc app=leetcode id=1248 lang=python3
#
# [1248] Count Number of Nice Subarrays
#
# https://leetcode.com/problems/count-number-of-nice-subarrays/description/
#
# algorithms
# Medium (55.64%)
# Likes:    386
# Dislikes: 11
# Total Accepted:    15.2K
# Total Submissions: 27.3K
# Testcase Example:  '[1,1,2,1,1]\n3'
#
# Given an array of integers nums and an integer k. A subarray is called nice
# if there are k odd numbers on it.
#
# Return the number of nice sub-arrays.
#
#
# Example 1:
#
#
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and
# [1,2,1,1].
#
#
# Example 2:
#
#
# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There is no odd numbers in the array.
#
#
# Example 3:
#
#
# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10^5
# 1 <= k <= nums.length
#
#
#
#TAGS sliding window
# trick we can't compute the exact number of window with exactly k numbers
#  (no monotonocity property)
# however we can compute atMost
#TODO too slow          

# @lc code=start
def atMost(nums, k):
    n = len(nums)
    res = 0
    j = 0
    count = 0
    for i in range(n):
        while j <= n and count <= k:
            if j <n and nums[j] % 2 == 1:
                count += 1
            j += 1

        res += j - i
        if nums[i] % 2 == 1:
            count -= 1
    return res

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return atMost(nums, k) - atMost(nums, k-1)
# @lc code=end

