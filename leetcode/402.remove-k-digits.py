#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#
# https://leetcode.com/problems/remove-k-digits/description/
#
# algorithms
# Medium (26.96%)
# Likes:    1087
# Dislikes: 66
# Total Accepted:    70.9K
# Total Submissions: 263.1K
# Testcase Example:  '"1432219"\n3'
#
# Given a non-negative integer num represented as a string, remove k digits
# from the number so that the new number is the smallest possible.
#
#
# Note:
#
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
#
#
#
#
# Example 1:
#
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219
# which is the smallest.
#
#
#
# Example 2:
#
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output
# must not contain leading zeroes.
#
#
#
# Example 3:
#
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with
# nothing which is 0.
#
#
#

# TAGS dp, hard
# I got the idea for dp part easily, but struggles on the details.
# I wanted to store an array [3, 20, 100] (little endian) but
# removing digits change the coefficient in the decimal representation.
# Quite a cool dp problem, harder than usual
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        memo = {}
        def f(i, k):
            res = memo.get((i, k))
            if res is not None:
                return res
            if k == 0:
                res = int(num[i:])
            elif n - i == k:
                res = 0
            else:
                # we're placing digit i, but there are k digits removed
                # after it, so its coefficient is `n-i-k-1` instead of
                # n - i - 1
                res = min(f(i+1, k-1), (10 ** (n - i - k - 1)) * int(num[i]) + f(i+1, k))
            memo[(i,k)] = res
            return res

        return str(f(0, k))

def test():
    s = Solution()
    print(s.removeKdigits("1432219", 3))
    print(s.removeKdigits("10200", 1))
    print(s.removeKdigits("10", 2))


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # we build the answer using a monotonic stack
        #
        # Example
        #
        # s = "1452", k = 2
        # st = 1, 4, 5
        # if we add 2, only 1, 2 should remain
        #
        res = []
        for v in num:
            while res and res[-1] > v and k:
                res.pop()
                k -= 1
            if v != '0' or res:
                res.append(v)
        while res and k:
            res.pop()
            k -= 1
        return ''.join(res) if res else '0'


# @lc code=end

