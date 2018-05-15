#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
#
# algorithms
# Medium (57.23%)
# Likes:    1009
# Dislikes: 31
# Total Accepted:    40.4K
# Total Submissions: 70.2K
# Testcase Example:  '[1,2,3,4,5,6,7,8,9,10]\n5'
#
# A conveyor belt has packages that must be shipped from one port to another
# within D days.
# 
# The i-th package on the conveyor belt has a weight of weights[i].  Each day,
# we load the ship with packages on the conveyor belt (in the order given by
# weights). We may not load more weight than the maximum weight capacity of the
# ship.
# 
# Return the least weight capacity of the ship that will result in all the
# packages on the conveyor belt being shipped within D days.
# 
# 
# 
# Example 1:
# 
# 
# Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
# Output: 15
# Explanation: 
# A ship capacity of 15 is the minimum to ship all the packages in 5 days like
# this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10
# 
# Note that the cargo must be shipped in the order given, so using a ship of
# capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6,
# 7), (8), (9), (10) is not allowed. 
# 
# 
# Example 2:
# 
# 
# Input: weights = [3,2,2,4,1,4], D = 3
# Output: 6
# Explanation: 
# A ship capacity of 6 is the minimum to ship all the packages in 3 days like
# this:
# 1st day: 3, 2
# 2nd day: 2, 4
# 3rd day: 1, 4
# 
# 
# Example 3:
# 
# 
# Input: weights = [1,2,3,1,1], D = 4
# Output: 3
# Explanation: 
# 1st day: 1
# 2nd day: 2
# 3rd day: 3
# 4th day: 1, 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= D <= weights.length <= 50000
# 1 <= weights[i] <= 500
# 
# 
#

# @lc code=start# TAGS bisect, indices, cool

def f(weights, capacity):
    res = 1
    cur = 0
    for v in weights:
        cur += v
        if cur > capacity:
           res += 1
           cur = v
    return res

assert f([1,2,3,4,5], 5) == 4
assert f([1,2,3,4,5], 6) == 3
assert f([1,2,3,4,5,1], 10) == 2

class Solution:
    def shipWithinDays(self, weights, D):
        a = max(weights)
        b = 50000
        while a < b:
            m = (a + b) // 2
            if f(weights, m) <= D:
                b = m
            else:
                a = m + 1
        return a

# @lc code=end

