#
# @lc app=leetcode id=727 lang=python3
#
# [727] Minimum Window Subsequence
#
# https://leetcode.com/problems/minimum-window-subsequence/description/
#
# algorithms
# Hard (41.36%)
# Likes:    613
# Dislikes: 33
# Total Accepted:    35.8K
# Total Submissions: 86.6K
# Testcase Example:  '"abcdebdde"\n"bde"'
#
# Given strings S and T, find the minimum (contiguous) substring W of S, so
# that T is a subsequence of W.
#
# If there is no such window in S that covers all characters in T, return the
# empty string "". If there are multiple such minimum-length windows, return
# the one with the left-most starting index.
#
# Example 1:
#
#
# Input:
# S = "abcdebdde", T = "bde"
# Output: "bcde"
# Explanation:
# "bcde" is the answer because it occurs before "bdde" which has the same
# length.
# "deb" is not a smaller window because the elements of T in the window must
# occur in order.
#
#
#
#
# Note:
#
#
# All the strings in the input will only contain lowercase letters.
# The length of S will be in the range [1, 20000].
# The length of T will be in the range [1, 100].
#
#
#
#

# @lc code=start
# Spent time trying to find a sliding window solution
# i.e for each j in range(n), find best solution ending in j
# Couldn't find adequate datastructure to represent window.
#
# Simple solution: for each i, find best solution O(n^2)
#
# Check better solutions TODO

def issubsequence(S, T, i):
    i -= 1
    first = None
    for c in T:
        i = S.find(c, i + 1)
        if i == -1:
            return None, None
        if first is None:
            first = i
    return first, i

class Solution:
    def minWindow(self, S: str, T: str) -> str:
        n = len(S)
        best = float('inf')
        res = 0, -1
        for i in range(n):
            first, last = issubsequence(S, T, i)
            if first is None:
                break
            if last - first < best:
                best = last - first
                res = first, last
        return S[res[0]: res[1]+1]

# DP find bug, 34/59 cases passed (TODO)
#
# class Solution:
#     def minWindow(self, S: str, T: str) -> str:
#         n = len(S)
#         p = len(T)
#         memo = [[None] * (p + 1) for _ in range(n+1)]
#         # memo[i][j] best solution for S[i:] and T[j:]
#         for j in range(p): # not recognized
#             memo[n][j] = 0, float('inf')
#         for i in range(n+1):
#             memo[i][p] = i, i
#         for i in reversed(range(n)):
#             for j in reversed(range(p)):

#                 u, v = memo[i+1][j]
#                 res = u, v

#                 if S[i] == T[j]:
#                     _, vv = memo[i+1][j+1]
#                     if vv - i < v - u or (vv - i == v - u) and i < u:
#                         res = i, vv

#                 memo[i][j] = res
#         i, j = memo[0][0]
#         return S[i:j] if j != float('inf') else ''





# @lc code=end

