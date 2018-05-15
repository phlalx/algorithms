#
# @lc app=leetcode id=330 lang=python3
#
# [330] Patching Array
#
# https://leetcode.com/problems/patching-array/description/
#
# algorithms
# Hard (34.26%)
# Likes:    470
# Dislikes: 71
# Total Accepted:    35.9K
# Total Submissions: 104.6K
# Testcase Example:  '[1,3]\n6'
#
# Given a sorted positive integer array nums and an integer n, add/patch
# elements to the array such that any number in range [1, n] inclusive can be
# formed by the sum of some elements in the array. Return the minimum number of
# patches required.
# 
# Example 1:
# 
# 
# Input: nums = [1,3], n = 6
# Output: 1 
# Explanation:
# Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3,
# 4.
# Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3],
# [2,3], [1,2,3].
# Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
# So we only need 1 patch.
# 
# Example 2:
# 
# 
# Input: nums = [1,5,10], n = 20
# Output: 2
# Explanation: The two patches can be [2, 4].
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,2], n = 5
# Output: 0
# 
#

# Tags greedy
#
# This is a cool greedy problem.
# The trick is to keep track of the longest interval that can be covered.
# [1, max_reach], and notice that the greedy thing to do to extend this interval
# is to add an element `max_reach + 1`. The new covered interval is then
# [1, 2 * max_reach + 1]

# TAGS TODO bad runtime

# @lc code=start

class Solution:
    def minPatches(self, nums: List[int], N: int) -> int:
        if not nums:
            nums = [1]
            res = 1
        else:
            res = 0
        max_reach = 0
        i = 0
        n = len(nums)
        while max_reach < N:
            # two ways to increase the reach
            #
            # 1. get a new element v that is not too large
            #    think [1 + v, max_reach + v]
            if i < n and nums[i] <= max_reach + 1:
                max_reach += nums[i]
                i += 1
            # 2. patch the array, greedy choice.
            #    We don't consume v as it may be useful in the future
            else:
                max_reach = 2 * max_reach + 1
                res +=1
        return res
# @lc code=end

