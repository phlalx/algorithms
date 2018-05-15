#
# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#
# https://leetcode.com/problems/sum-of-subarray-minimums/description/
#
# algorithms
# Medium (29.03%)
# Likes:    826
# Dislikes: 58
# Total Accepted:    19.2K
# Total Submissions: 62.7K
# Testcase Example:  '[3,1,2,4]'
#
# Given an array of integers A, find the sum of min(B), where B ranges over
# every (contiguous) subarray of A.
#
# Since the answer may be large, return the answer modulo 10^9 + 7.
#
#
#
# Example 1:
#
#
# Input: [3,1,2,4]
# Output: 17
# Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2],
# [1,2,4], [3,1,2,4].
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
#
#
#
# Note:
#
#
# 1 <= A.length <= 30000
# 1 <= A[i] <= 30000
#
#
#
#
#
#
#
# There is an obvious solution in O(n^2).
# If we want to do better than that, we must *not* scan all pair (i, j).
# Suppose we scan the array from left to right, we would like to compute
# at once all the min for all sub-arrays ending in i
#
# Consider this example
#
# [1, 4, 2, 6, 5 ...
#        i
#
# No need to consider "4" since A[i] = 2 < 4
# We can consider only the subsequence [1, 2] (more precisely, the indices)
#
# [1, 4, 2, 6, 5 ....
#              i
#
# We remember [1, 2, 5]
#
# From the stack, we can compute the sum of all mins
# However, we need an augmented data structure in order to have the sum of mins
# in constant time

#TAGS cool, monotonic stack
# Trick 

# @lc code=start
class Solution:
    def sumSubarrayMins(self, A):
        st = []
        res = 0
        stack_sum = 0
        for i, v in enumerate(A):
            while st and A[st[-1]] >= v:
                j = st.pop()
                stack_sum -= (A[j] * (j - st[-1]) if st else A[j] * (j + 1))
            stack_sum += (A[i] * (i - st[-1]) if st else A[i] * (i + 1))
            st.append(i)
            res += stack_sum
        return res % (10 ** 9 + 7)

# @lc code=end

