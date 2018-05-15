#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#
# https://leetcode.com/problems/integer-to-roman/description/
#
# algorithms
# Medium (52.01%)
# Likes:    839
# Dislikes: 2380
# Total Accepted:    309.8K
# Total Submissions: 578.6K
# Testcase Example:  '3'
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D
# and M.
#
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# For example, two is written as II in Roman numeral, just two one's added
# together. Twelve is written as, XII, which is simply X + II. The number
# twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. There
# are six instances where subtraction is used:
#
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
#
#
# Given an integer, convert it to a roman numeral. Input is guaranteed to be
# within the range from 1 to 3999.
#
# Example 1:
#
#
# Input: 3
# Output: "III"
#
# Example 2:
#
#
# Input: 4
# Output: "IV"
#
# Example 3:
#
#
# Input: 9
# Output: "IX"
#
# Example 4:
#
#
# Input: 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
#
#
# Example 5:
#
#
# Input: 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
#
# Trick: each digit in the source number correspond to a roman digit
#        pattern is always the same, only the letters change
#        I, V
#        X, L
#        ...
#
# @lc code=start

digit = ['I', 'V', 'X', 'L', 'C', 'D', 'M',  None, None] # Sentinel
value = [  1,   5, 10,  50,  100, 500, 1000, 5000, 10000]

def f(x, i):
    upper = digit[2 * i + 2]
    medium = digit[2 * i + 1]
    lower = digit[2 * i]
    if x in {1, 2, 3}:
        return x * lower
    elif x == 4:
        return lower + medium
    elif x == 5:
        return medium
    elif x in {6, 7, 8}:
        return medium + (x - 5) * lower
    else:
        return lower + upper

class Solution:

    def intToRoman(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = str(s)
        n = len(s)
        i = n - 1
        res = []
        # we parse big endian
        for d in s:
            if d != '0':
                # we need the power of the digit
                res.append(f(int(d), i))
            i -= 1

        return ''.join(res)


# @lc code=end

