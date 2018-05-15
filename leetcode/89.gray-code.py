# TAGS tree walk, path
# works recursively
# Suppose we know the answer for n = 2
# 0
# 3
# 2
# 1
#
# We append a 0, then append a 1 to the reversed list
# This can be done in O(n) space using a tree


# got the idea pretty quickly,
#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#
# https://leetcode.com/problems/gray-code/description/
#
# algorithms
# Medium (46.64%)
# Likes:    457
# Dislikes: 1312
# Total Accepted:    144.7K
# Total Submissions: 308.3K
# Testcase Example:  '2'
#
# The gray code is a binary numeral system where two successive values differ
# in only one bit.
#
# Given a non-negative integer n representing the total number of bits in the
# code, print the sequence of gray code. A gray code sequence must begin with
# 0.
#
# Example 1:
#
#
# Input: 2
# Output: [0,1,3,2]
# Explanation:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
#
# For a given n, a gray code sequence may not be uniquely defined.
# For example, [0,2,3,1] is also a valid gray code sequence.
#
# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1
#
#
# Example 2:
#
#
# Input: 0
# Output: [0]
# Explanation: We define the gray code sequence to begin with 0.
# A gray code sequence of n has size = 2^n, which for n = 0 the size is 2^0 =
# 1.
# Therefore, for n = 0 the gray code sequence is [0].
#
#
#

# @lc code=start


class Solution:
    def grayCode(self, n):
        if n == 0:
            return [0]
        res = []
        def f(i, reverse, path):
            if i == 0:
                res.append(path)
            else:
                a, b = 0, 1
                if reverse:
                    f(i-1, reverse, 2 * path + a)
                    f(i-1, not reverse, 2 * path + b)
                else:
                    f(i-1, not reverse, 2 * path + b)
                    f(i-1, reverse, 2 * path + a)
        f(n, True, 0)
        return res

# print(Solution().grayCode(2))
# print(Solution().grayCode(3))
# print(Solution().grayCode(4))

# @lc code=end

