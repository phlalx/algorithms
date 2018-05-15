#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#
# https://leetcode.com/problems/reorganize-string/description/
#
# algorithms
# Medium (43.70%)
# Likes:    719
# Dislikes: 37
# Total Accepted:    37.4K
# Total Submissions: 84.5K
# Testcase Example:  '"aab"'
#
# Given a string S, check if the letters can be rearranged so that two
# characters that are adjacent to each other are not the same.
#
# If possible, output any possible result.  If not possible, return the empty
# string.
#
# Example 1:
#
#
# Input: S = "aab"
# Output: "aba"
#
#
# Example 2:
#
#
# Input: S = "aaab"
# Output: ""
#
#
# Note:
#
#
# S will consist of lowercase letters and have length in range [1, 500].
#
#
#
#
#

# @lc code=start

#TAGS greedy
# not sure why it works
# sorting by frequency
# aabbac -> aaaabbc
# then fill the array 2 by 2
#
# Suppose a has the greatest frequency
# If there is a solution, we can write it
# a.a.a.a.....
#  X X X   Y
# Now we have x remaining letters to place. We can put anything
# in the X.
# Suppose b is the second most common letter.
# ... I'm stuck here TODO
# https://www.careercup.com/question?id=5693863291256832


from collections import Counter

class Solution:
    def reorganizeString(self, S: str) -> str:
        c = Counter(S)
        n = len(S)
        # trick use `x` in the key, otherwise the sort
        # doesn't work when two elements have the same frequency
        l = sorted(S, key = lambda x: (c[x], x), reverse=True)
        i = 0
        res = [ None ] * n
        # pythonic, we could use slices here
        for c in l:
            res[i] = c
            i += 2
            if i >= n:
                i = 1
        for c, d in zip(res, res[1:]):
            if c == d:
                return ""
        return ''.join(res)


# @lc code=end

