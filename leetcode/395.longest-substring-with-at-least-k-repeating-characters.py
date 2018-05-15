#
# @lc app=leetcode id=395 lang=python3
#
# [395] Longest Substring with At Least K Repeating Characters
#
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
#
# algorithms
# Medium (39.32%)
# Likes:    1091
# Dislikes: 94
# Total Accepted:    64.6K
# Total Submissions: 160.9K
# Testcase Example:  '"aaabb"\n3'
#
#
# Find the length of the longest substring T of a given string (consists of
# lowercase letters only) such that every character in T appears no less than k
# times.
#
#
# Example 1:
#
# Input:
# s = "aaabb", k = 3
#
# Output:
# 3
#
# The longest substring is "aaa", as 'a' is repeated 3 times.
#
#
#
# Example 2:
#
# Input:
# s = "ababbc", k = 2
#
# Output:
# 5
#
# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is
# repeated 3 times.
#
#
#

# @lc code=start
# TAGS divide and conquer
# divide and conquer: trick -> pivot is not middle!
# we discard any string that contain a char present less than k times
# so we can just split and consider left and right substring

# a a b c b, k = 2
# a a a b b c b, k = 3

from collections import Counter

# divide and conquer (pythonic)
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:
                return max((self.longestSubstring(ss, k)
                           for ss in s.split(c)), default=0)
        return len(s)


# @lc code=end

