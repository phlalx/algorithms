#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#
# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
#
# algorithms
# Medium (48.10%)
# Likes:    819
# Dislikes: 66
# Total Accepted:    31.9K
# Total Submissions: 66.1K
# Testcase Example:  '[4,5,0,-2,-3,1]\n5'
#
# Given an array A of integers, return the number of (contiguous, non-empty)
# subarrays that have a sum divisible by K.
#
#
#
#
# Example 1:
#
#
# Input: A = [4,5,0,-2,-3,1], K = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by K = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2,
# -3]
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 30000
# -10000 <= A[i] <= 10000
# 2 <= K <= 10000
#
#
#

# @lc code=start
#TAGS 2-sum
# identical to sum array is k, except that we work modulo K

# see 523 for a more complicated variant
from collections import Counter

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        cur = 0
        prev = [1] + [0] * (K - 1)
        res = 0
        for v in A:
            cur = (cur + v) % K
            res += prev[cur]
            prev[cur] += 1
        return res


# @lc code=end

