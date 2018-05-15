#
# @lc app=leetcode id=280 lang=python3
#
# [280] Wiggle Sort
#
# https://leetcode.com/problems/wiggle-sort/description/
#
# algorithms
# Medium (61.63%)
# Likes:    448
# Dislikes: 48
# Total Accepted:    71.2K
# Total Submissions: 115.5K
# Testcase Example:  '[3,5,2,1,6,4]'
#
# Given an unsorted array nums, reorder it in-place such that nums[0] <=
# nums[1] >= nums[2] <= nums[3]....
#
# TAGS https://leetcode.com/problems/wiggle-sort-ii/discuss/77684/Summary-of-the-various-solutions-to-Wiggle-Sort-for-your-reference
# TAGS wiggle
# do the remapping in place is hard TODO
# Example:
#
#
# Input: nums = [3,5,2,1,6,4]
# Output: One possible answer is [3,5,1,6,2,4]
#
#
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        res = []
        n = len(nums)
        i = 0
        j = n - 1
        b = True
        while i <= j:
            if b:
                res.append(nums[i])
                i += 1
            else:
                res.append(nums[j])
                j -= 1
            b = not b
        nums[:] = res[:]
        return res



