#
# @lc app=leetcode id=1358 lang=python3
#
# [1358] Number of Substrings Containing All Three Characters
#
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/
#
# algorithms
# Medium (55.90%)
# Likes:    320
# Dislikes: 4
# Total Accepted:    9.5K
# Total Submissions: 16.6K
# Testcase Example:  '"abcabc"'
#
# Given a string s consisting only of characters a, b and c.
#
# Return the number of substrings containing at least one occurrence of all
# these characters a, b and c.
#
#
# Example 1:
#
#
# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the
# characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab",
# "bcabc", "cab", "cabc" and "abc" (again).
#
#
# Example 2:
#
#
# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the
# characters a, b and c are "aaacb", "aacb" and "acb".
#
#
# Example 3:
#
#
# Input: s = "abc"
# Output: 1
#
#
#
# Constraints:
#
#
# 3 <= s.length <= 5 x 10^4
# s only consists of a, b or c characters.
#
#
#TAGS sliding window
#

# @lc code=start

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        counter = {'a': 0, 'b': 0, 'c': 0}
        res = 0
        i = 0
        for j in range(n):
            counter[s[j]] += 1
            while all(counter.values()):
                counter[s[i]] -= 1
                i += 1
            res += i
        return res

# @lc code=end

