#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#
# https://leetcode.com/problems/sort-array-by-parity/description/
#
# algorithms
# Easy (72.75%)
# Likes:    670
# Dislikes: 67
# Total Accepted:    151.3K
# Total Submissions: 206.1K
# Testcase Example:  '[3,1,2,4]'
#
# Given an array A of non-negative integers, return an array consisting of all
# the even elements of A, followed by all the odd elements of A.
# 
# You may return any answer array that satisfies this condition.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000
# 
# 
# 
#

# @lc code=start
# class Solution:
#     def sortArrayByParity(self, A: List[int]) -> List[int]:
#         A.sort(key = lambda x: x % 2)
#         return A

# TAGS queue
# Trick insert even element on the left, odd elements on the right

from collections import deque

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        res = deque()
        for v in A:
            if v % 2 == 0:
                res.appendleft(v)
            else:
                res.append(v)
        return list(res)

# @lc code=end

