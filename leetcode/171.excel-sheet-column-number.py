#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#
# https://leetcode.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (52.24%)
# Likes:    733
# Dislikes: 132
# Total Accepted:    255.3K
# Total Submissions: 481.6K
# Testcase Example:  '"A"'
#
# Given a column title as appear in an Excel sheet, return its corresponding
# column number.
#
# For example:
#
#
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28
# ⁠   ...
#
#
# Example 1:
#
#
# Input: "A"
# Output: 1
#
#
# Example 2:
#
#
# Input: "AB"
# Output: 28
#
#
# Example 3:
#
#
# Input: "ZY"
# Output: 701
#
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for c in s:
            res = (26 * res) + ord(c) - ord('A') + 1
        return res


# @lc code=end

