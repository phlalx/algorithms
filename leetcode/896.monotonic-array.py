#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#
# https://leetcode.com/problems/monotonic-array/description/
#
# algorithms
# Easy (55.73%)
# Likes:    423
# Dislikes: 31
# Total Accepted:    73.7K
# Total Submissions: 130.1K
# Testcase Example:  '[1,2,2,3]'
#
# An array is monotonic if it is either monotone increasing or monotone
# decreasing.
# 
# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array
# A is monotone decreasing if for all i <= j, A[i] >= A[j].
# 
# Return true if and only if the given array A is monotonic.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,2,3]
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: [6,5,4,4]
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# Input: [1,3,2]
# Output: false
# 
# 
# 
# Example 4:
# 
# 
# Input: [1,2,4,5]
# Output: true
# 
# 
# 
# Example 5:
# 
# 
# Input: [1,1,1]
# Output: true
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 50000
# -100000 <= A[i] <= 100000
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        sign = 0
        for u, v in zip(A, A[1:]):
            if sign * (v - u) < 0:
                return False
            if v - u != 0:
                sign = v - u
        return True

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        inc = False
        dec = False
        for c, cc in zip(A, A[1:]):
            if c < cc:
                inc = True
            elif c > cc:
                dec = True
        return not (inc and dec)

        
# @lc code=end

