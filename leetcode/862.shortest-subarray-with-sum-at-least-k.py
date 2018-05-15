#
# @lc app=leetcode id=862 lang=python3
#
# [862] Shortest Subarray with Sum at Least K
#
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/
#
# algorithms
# Hard (22.65%)
# Likes:    761
# Dislikes: 22
# Total Accepted:    21.8K
# Total Submissions: 93.9K
# Testcase Example:  '[1]\n1'
#
# Return the length of the shortest, non-empty, contiguous subarray of A with
# sum at least K.
#
# If there is no non-empty subarray with sum at least K, return -1.
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
# Input: A = [1], K = 1
# Output: 1
#
#
#
# Example 2:
#
#
# Input: A = [1,2], K = 4
# Output: -1
#
#
#
# Example 3:
#
#
# Input: A = [2,-1,2], K = 3
# Output: 3
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 50000
# -10 ^ 5 <= A[i] <= 10 ^ 5
# 1 <= K <= 10 ^ 9
#
#
#
#
#
#

# @lc code=start
#TAGS sliding window, monotonic queue
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/189039/Detailed-intuition-behind-Deque-solution
# Generalize 209
# classic
#
# Remember this:
#
# For each j, we want to find the nearest i such that aj - ai >= k
# This is a good overview of monotonic queue problems
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/204290/Monotonic-Queue-Summary


from collections import deque

class Solution:
    # sliding window is failing here
    # there's no monocity propertys
    # def shortestSubarray(self, A: List[int], K: int) -> int:
    #     n = len(A)
    #     i = 0
    #     j = 0
    #     pred = lambda i, j: sum(A[i:j+1]) >= K
    #     best = float('inf')
    #     while j < n:
    #         while i < n and pred(i, j):
    #             best = min(best, j - i + 1)
    #             i += 1
    #         j += 1
    #     return best if best != float('inf') else -1

    def shortestSubarray(self, A, K):
        N = len(A)
        B = [0] * (N + 1)
        for i in range(N):
            B[i + 1] = B[i] + A[i]
        d = deque()
        res = N + 1
        for i in range(N + 1):
            # This is more original, we remove elements on the
            # left part
            while d and B[i] - B[d[0]] >= K:
                res = min(res, i - d.popleft())
            # classic: maintain an increasing queue
            # We remove candidates that are rendered useless by B[i]
            while d and B[i] <= B[d[-1]]:
                d.pop()
            d.append(i)
        return res if res <= N else -1

# @lc code=end