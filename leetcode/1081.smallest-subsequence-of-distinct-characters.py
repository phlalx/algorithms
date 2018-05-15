#
# @lc app=leetcode id=1081 lang=python3
#
# [1081] Smallest Subsequence of Distinct Characters
#
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description/
#
# algorithms
# Medium (48.77%)
# Likes:    357
# Dislikes: 62
# Total Accepted:    9.8K
# Total Submissions: 19.9K
# Testcase Example:  '"cdadabcc"'
#
# Return the lexicographically smallest subsequence of text that contains all
# the distinct characters of text exactly once.
#
# Example 1:
#
#
# Input: "cdadabcc"
# Output: "adbc"
#
#
#
# Example 2:
#
#
# Input: "abcd"
# Output: "abcd"
#
#
#
# Example 3:
#
#
# Input: "ecbacba"
# Output: "eacb"
#
#
#
# Example 4:
#
#
# Input: "leetcode"
# Output: "letcod"
#
#
#
#
# Constraints:
#
#
# 1 <= text.length <= 1000
# text consists of lowercase English letters.
#
#
# Note: This question is the same as 316:
# https://leetcode.com/problems/remove-duplicate-letters/
#
#
#
#
#
# TAGS monotonous stack
#   hard to find the trick
#   my first thought was DP with bitset, but seemed overkill
#   second idea is to find greedily each char, it works but is suboptimal.
#   Two tricks to remember
#   1. construct the result using a stack (think monotonous stack in the way
#     we append and pop)
#   2. keep the last index of each char
#
#   Using these tricks, the algorithm follows:
#   . consider all letters in order
#   . ignore those already in the solution
#   . we can safely remove the last element of the stack if it appears later
#   Even with the first hint, I wasn't unable to find the second trick
#

# @lc code=start

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # keep last index for each letter
        indices = {c: i for i, c in enumerate(s)}
        res = []
        for i, c in enumerate(s):
            if c in res:
                continue
            while (res and c < res[-1]
                   and indices.get(res[-1], float('-inf')) > i):
                res.pop()
            res.append(c)
        return ''.join(res)

# @lc code=end

