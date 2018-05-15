#
# @lc app=leetcode id=992 lang=python3
#
# [992] Subarrays with K Different Integers
#
# https://leetcode.com/problems/subarrays-with-k-different-integers/description/
#
# algorithms
# Hard (45.17%)
# Likes:    683
# Dislikes: 13
# Total Accepted:    19.2K
# Total Submissions: 41.3K
# Testcase Example:  '[1,2,1,2,3]\n2'
#
# Given an array A of positive integers, call a (contiguous, not necessarily
# distinct) subarray of A good if the number of different integers in that
# subarray is exactly K.
#
# (For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)
#
# Return the number of good subarrays of A.
#
#
#
# Example 1:
#
#
# Input: A = [1,2,1,2,3], K = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2],
# [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
#
#
# Example 2:
#
#
# Input: A = [1,2,1,3,4], K = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3],
# [2,1,3], [1,3,4].
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 20000
# 1 <= A[i] <= A.length
# 1 <= K <= A.length
#
#

#TAG sliding window
#trick reduce to atMost

# @lc code=start
from collections import Counter
from typing import List

def atMost(A, K):
    i = 0
    j = 0
    n = len(A)
    count = Counter()
    distinct = 0  # initial empty window [i,j)
    res = 0
    for i in range(n):

        # find first j for which p(i,j) doesn't hold
        while j <= n and distinct <= K:
            # add j in window and recompute property
            if j < n:
                if count[A[j]] == 0:
                    distinct += 1
                count[A[j]] += 1
            j += 1

        res += j - i

        # remove i from window and recompute property
        if count[A[i]] == 1:
            distinct -= 1
        count[A[i]] -= 1

    return res

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return atMost(A, K) - atMost(A, K-1)

# @lc code=end

