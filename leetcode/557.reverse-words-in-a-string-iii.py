#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#
# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
#
# algorithms
# Easy (65.19%)
# Likes:    788
# Dislikes: 80
# Total Accepted:    167.5K
# Total Submissions: 250.2K
# Testcase Example:  `"Let's take LeetCode contest"`
#
# Given a string, you need to reverse the order of characters in each word
# within a sentence while still preserving whitespace and initial word order.
# 
# Example 1:
# 
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# 
# 
# 
# Note:
# In the string, each word is separated by single space and there will not be
# any extra space in the string.
# 
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        return ' '.join([w[::-1] for w in l])
        
# @lc code=end

