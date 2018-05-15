#
# @lc app=leetcode id=434 lang=python3
#
# [434] Number of Segments in a String
#
# https://leetcode.com/problems/number-of-segments-in-a-string/description/
#
# algorithms
# Easy (37.22%)
# Likes:    161
# Dislikes: 619
# Total Accepted:    63.8K
# Total Submissions: 171K
# Testcase Example:  '"Hello, my name is John"'
#
# Count the number of segments in a string, where a segment is defined to be a
# contiguous sequence of non-space characters.
#
# Please note that the string does not contain any non-printable characters.
#
# Example:
#
# Input: "Hello, my name is John"
# Output: 5
#
#
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        res = 0
        prev = ' '
        for cur in s:
            if cur != ' ' and prev == ' ':
                res += 1
            prev = cur
        return res

# @lc code=end

