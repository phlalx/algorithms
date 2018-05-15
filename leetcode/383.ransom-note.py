#TAGS multiset inclusion

# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note/description/
#
# algorithms
# Easy (50.64%)
# Likes:    374
# Dislikes: 142
# Total Accepted:    128.7K
# Total Submissions: 252.5K
# Testcase Example:  '"a"\n"b"'
#
#
# Given an arbitrary ransom note string and another string containing letters
# from all the magazines, write a function that will return true if the ransom
# note can be constructed from the magazines ; otherwise, it will return
# false.
#
#
# Each letter in the magazine string can only be used once in your ransom
# note.
#
#
# Note:
# You may assume that both strings contain only lowercase letters.
#
#
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
#
#
#

# @lc code=start

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = Counter(magazine)
        for c in ransomNote:
            if letters[c] == 0:
                return False
            else:
                letters[c] -= 1
        return True

# constant space solution

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)
        j = 0
        p = len(magazine)
        for c in ransomNote:
            while j < p and magazine[j] < c:
                j += 1
            if j == p or magazine[j] > c:
                return False
            else:
                j += 1
        return True


# @lc code=end

