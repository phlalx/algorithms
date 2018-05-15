#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (28.81%)
# Likes:    7781
# Dislikes: 458
# Total Accepted:    1.3M
# Total Submissions: 4.5M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
# 
#

# @lc code=start
#TAGS sliding window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        j = 0
        best = 0
        seen = set()
        for i in range(n):
            while j < n and s[j] not in seen:
                seen.add(s[j])
                j += 1
            best = max(best, j - i)
            seen.remove(s[i])
        return best


# @lc code=end

