#
# @lc app=leetcode id=925 lang=python3
#
# [925] Long Pressed Name
#
# https://leetcode.com/problems/long-pressed-name/description/
#
# algorithms
# Easy (44.56%)
# Likes:    382
# Dislikes: 50
# Total Accepted:    28.2K
# Total Submissions: 63.3K
# Testcase Example:  '"alex"\n"aaleex"'
#
# Your friend is typing his name into a keyboard.  Sometimes, when typing a
# character c, the key might get long pressed, and the character will be typed
# 1 or more times.
# 
# You examine the typed characters of the keyboard.  Return True if it is
# possible that it was your friends name, with some characters (possibly none)
# being long pressed.
# 
# 
# 
# Example 1:
# 
# 
# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.
# 
# 
# 
# Example 2:
# 
# 
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it wasn't in the typed
# output.
# 
# 
# 
# Example 3:
# 
# 
# Input: name = "leelee", typed = "lleeelee"
# Output: true
# 
# 
# 
# Example 4:
# 
# 
# Input: name = "laiden", typed = "laiden"
# Output: true
# Explanation: It's not necessary to long press any character.
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# name.length <= 1000
# typed.length <= 1000
# The characters of name and typed are lowercase letters.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        def bla(s):
            n = len(s)
            i = 0
            while i < n:
                c = s[i]
                count = 1
                while i < n and s[i] == c:
                    count += 1
                    i += 1
                yield c, count

        it1 = bla(name)
        it2 = bla(typed)
        for x, i in it1:
            y, j = next(it2, (None, None))
            if y is None or x != y or i > j:
                return False
        return next(it2, None) is None

        
# @lc code=end

