#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#
# https://leetcode.com/problem  s/find-all-duplicates-in-an-array/description/
#
# algorithms
# Medium (62.17%)
# Likes:    1364
# Dislikes: 125
# Total Accepted:    119.7K
# Total Submissions: 190.7K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements
# appear twice and others appear once.
#
# Find all the elements that appear twice in this array.
#
# Could you do it without extra space and in O(n) runtime?
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [2,3]
#
#

# @lc code=start
# Tags array
# Trick: store two values at the same index.
# 

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        upper = n + 1
        # all v in nums lower than upper

        for v in nums:
            v = (v - 1) % upper
            if nums[v] // upper:
                res.append(v+1)
            else:
                nums[v] += upper

        return res


# @lc code=end

