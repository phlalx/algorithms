# # TAGS binary search, linear scan
# http://blog.ruofeidu.com/719-find-k-th-smallest-pair-distance/
#
# @lc app=leetcode id=719 lang=python3
#
# [719] Find K-th Smallest Pair Distance
#
# https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/
#
# algorithms
# Hard (31.09%)
# Likes:    873
# Dislikes: 34
# Total Accepted:    31.1K
# Total Submissions: 99.9K
# Testcase Example:  '[1,3,1]\n1'
#
# Given an integer array, return the k-th smallest distance among all the
# pairs. The distance of a pair (A, B) is defined as the absolute difference
# between A and B.
#
# Example 1:
#
# Input:
# nums = [1,3,1]
# k = 1
# Output: 0
# Explanation:
# Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.
#
#
#
# Note:
#
# 2 .
# 0 .
# 1 .
#
#
# 


 
# @lc code=start

# A generic binary search
# return the first element  in [i:j+1] such that pred is True
# return j+1 if no such element exists
def binary_search(i, j, pred):
    while i < j:
        m = (i + j) // 2
        if pred(m):
            j = m
        else:
            i = m + 1
    return i if pred(i) else i + 1

def count(nums, target):
    n = len(nums)
    j = 0
    res = 0
    for i in range(n):
        while j < n and nums[j] - nums[i] <= target:
            res += j - i
            j += 1
    return res

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        pred = lambda target: count(nums, target) >= k
        target_max = nums[-1] - nums[0]
        res = binary_search(0, target_max, pred)
        return res

# @lc code=end

