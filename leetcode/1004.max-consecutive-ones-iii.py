#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#
# https://leetcode.com/problems/max-consecutive-ones-iii/description/
#
# algorithms
# Medium (54.61%)
# Likes:    373
# Dislikes: 7
# Total Accepted:    19.7K
# Total Submissions: 35.8K
# Testcase Example:  '[1,1,1,0,0,0,1,1,1,1,0]\n2'
#
# Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
#
# Return the length of the longest (contiguous) subarray that contains only
# 1s. 
#
#
#
#
# Example 1:
#
#
# Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# Output: 6
# Explanation:
# [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is
# underlined.
#
#
# Example 2:
#
#
# Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# Output: 10
# Explanation:
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is
# underlined.
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 20000
# 0 <= K <= A.length
# A[i] is 0 or 1 
#
#
#
#
#

# TAGS dp, sliding window
# dp is too slow, sliding window is the natural solution

# @lc code=start
# class Solution:
#     def longestOnes(self, A: List[int], K: int) -> int:
#         n = len(A)
#         memo = {}
#         def f(i, k):
#             res = memo.get((i, k))
#             if res is not None:
#                 return res
#             if i == n:
#                 res = 0
#             else:
#                 res = 0
#                 if A[i] == 1:
#                     res = 1 + f(i+1, k)
#                 elif A[i] == 0 and k >= 1:
#                     res = 1 + f(i+1, k-1)
#             memo[(i, k)] = res
#             return res
#         return max(f(i, K) for i in range(n))

# Solution 1
# For each i, find the longest substring starting in i

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        res = 0
        j = 0
        k = K
        n = len(A)
        for i in range(n):
            while j < n and (A[j] == 1 or k > 0):
                res = max(res, j - i + 1)
                k -= A[j] == 0
                j += 1
            k += A[i] == 0
        return res

# Solution 2
# For each j, find the longest substring ending in j
#
# If we look at the matrix Mij = [  is_good(A[i:j+1]) ], the difference
# between solution 1 and 2, is the traversal order of the matrix
# line first, or column first.

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        res = 0
        i = 0
        n = len(A)
        switched = 0
        for j in range(n):
            switched += A[j] == 0
            while i <= j and switched > K:
                switched -= A[i] == 0
                i += 1
            res = max(res, j - i + 1)
        return res

# # @lc code=end

