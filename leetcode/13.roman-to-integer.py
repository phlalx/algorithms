#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#
# https://leetcode.com/problems/roman-to-integer/description/
#
# algorithms
# Easy (53.20%)
# Likes:    1765
# Dislikes: 3201
# Total Accepted:    587.4K
# Total Submissions: 1.1M
# Testcase Example:  '"III"'
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
# Given a roman numeral, convert it to an integer. Input is guaranteed to be
# within the range from 1 to 3999.
#
# Example 1:
#
#
# Input: "III"
# Output: 3
#
# Example 2:
#
#
# Input: "IV"
# Output: 4
#
# Example 3:
#
#
# Input: "IX"
# Output: 9
#
# Example 4:
#
#
# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
#
#
# Example 5:
#
#
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
#

# @lc code=start

def parse(s, i, a, b, c):
    n = len(s)
    if i + 3 < n and s[i:i+4] == b + a + a + a:
        return i+4, 8
    elif i + 2 < n and s[i:i+3] == b + a + a:
        return i+3, 7
    elif i + 2 < n and s[i:i+3] == a + a + a:
        return i+3, 3
    elif i + 1 < n and s[i:i+2] == b + a:
        return i+2, 6
    elif i + 1 < n and s[i:i+2] == a + b:
        return i+2, 4
    elif i + 1 < n and s[i:i+2] == a + a:
        return i+2, 2
    elif i + 1 < n and s[i:i+2] == a + c:
        return i+2, 9
    elif i < n and s[i] == a:
        return i+1, 1
    elif i < n and s[i] == b:
        return i+1, 5
    else:
        assert 0

# Trick
# Parse digit per digit, LL(1)
# we know each power of ten we are parsing, based on first symbol
# I II III IV V VI VII VIII IX
# X XX XXX XL L LX LXX LXXX XC

class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        n = len(s)
        res = 0
        while i < n:
            c = s[i]
            if c in {'I', 'V'}:
                i, l = parse(s, i, 'I', 'V', 'X')
                res += l
            elif c in {'X', 'L'}:
                i, l = parse(s, i, 'X', 'L', 'C')
                res += 10 * l
            elif c in {'C', 'D'}:
                i, l = parse(s, i, 'C', 'D', 'M')
                res += 100 * l
            elif c == 'M':
                i, l = parse(s, i, 'M', 'A', 'B')
                res += 1000 * l
            else:
                assert 0

        return res


# @lc code=end

