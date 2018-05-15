#
# @lc app=leetcode id=926 lang=python3
#
# [926] Flip String to Monotone Increasing
#
# https://leetcode.com/problems/flip-string-to-monotone-increasing/description/
#
# algorithms
# Medium (50.36%)
# Likes:    460
# Dislikes: 15
# Total Accepted:    18K
# Total Submissions: 35K
# Testcase Example:  '"00110"'
#
# A string of '0's and '1's is monotone increasing if it consists of some
# number of '0's (possibly 0), followed by some number of '1's (also possibly
# 0.)
#
# We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or
# a '1' to a '0'.
#
# Return the minimum number of flips to make S monotone increasing.
#
#
#
#
# Example 1:
#
#
# Input: "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.
#
#
#
# Example 2:
#
#
# Input: "010110"
# Output: 2
# Explanation: We flip to get 011111, or alternatively 000111.
#
#
#
# Example 3:
#
#
# Input: "00011000"
# Output: 2
# Explanation: We flip to get 00000000.
#
#
#
#
# Note:
#
#
# 1 <= S.length <= 20000
# S only consists of '0' and '1' characters.
#
#
#
#
#

# @lc code=start
#TAGS dp

class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        n = len(S)
        cur = 0
        res = 0
        for i in reversed(range(n)):
            if S[i] == '1':
                res = min(res + 1, cur)
            else:
                cur += 1
        return res


# @lc code=end
