#
# @lc app=leetcode id=961 lang=python3
#
# [961] N-Repeated Element in Size 2N Array
#
# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/
#
# algorithms
# Easy (72.41%)
# Likes:    316
# Dislikes: 189
# Total Accepted:    91.6K
# Total Submissions: 125.8K
# Testcase Example:  '[1,2,3,3]'
#
# In a array A of size 2N, there are N+1 unique elements, and exactly one of
# these elements is repeated N times.
#
# Return the element repeated N times.
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
# Input: [1,2,3,3]
# Output: 3
#
#
#
# Example 2:
#
#
# Input: [2,1,2,5,3,2]
# Output: 2
#
#
#
# Example 3:
#
#
# Input: [5,1,5,2,5,3,5,4]
# Output: 5
#
#
#
#
# Note:
#
#
# 4 <= A.length <= 10000
# 0 <= A[i] < 10000
# A.length is even
#
#
#
#
#
#
#TAGS set
#TODO see if constant space solution

# @lc code=start
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        seen = set()
        for n in A:
            if n in seen:
                return n
            seen.add(n)
        assert 0

# @lc code=end

