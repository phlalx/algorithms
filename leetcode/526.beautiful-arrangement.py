#
# @lc app=leetcode id=526 lang=python3
#
# [526] Beautiful Arrangement
#
# https://leetcode.com/problems/beautiful-arrangement/description/
#
# algorithms
# Medium (55.49%)
# Likes:    543
# Dislikes: 134
# Total Accepted:    44.7K
# Total Submissions: 79.1K
# Testcase Example:  '2'
#
# Suppose you have N integers from 1 to N. We define a beautiful arrangement as
# an array that is constructed by these N numbers successfully if one of the
# following is true for the ith position (1 <= i <= N) in this array:
#
#
# The number at the ith position is divisible by i.
# i is divisible by the number at the ith position.
#
#
#
#
# Now given N, how many beautiful arrangements can you construct?
#
# Example 1:
#
#
# Input: 2
# Output: 2
# Explanation:
#
# The first beautiful arrangement is [1, 2]:
#
# Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
#
# Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
#
# The second beautiful arrangement is [2, 1]:
#
# Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
#
# Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
#
#
#
#
# Note:
#
#
# N is a positive integer and will not exceed 15.
#


#TAGS backtracking, bitset, brute force
# not so cool, but classic, not many problems using bitsets

def bits(s, N):
    for i in range(N):
        if s & (1 << i):
            yield i

class Solution:
    def countArrangement(self, N):
        def f(i, s):
            print(i, s)
            res = 0
            if i == 1:
                res = 1
            else:
                for x in bits(s, N):
                    j = x + 1
                    if j % i == 0 or i % j == 0:
                        res += f(i-1, s & ~(1 << x))
            return res

        available_bits = (1 << N) - 1
        return f(N, available_bits)

class Solution:
    def countArrangement(self, N):
        perm = []
        res = 0
        def f(i):
          nonlocal res
          if i == N+1:
            res += 1
          else:
            for v in range(1,N+1):
                if v not in perm and ((v % i == 0) or (i % v == 0)):
                    perm.append(v)
                    f(i+1)
                    perm.pop()
        f(1)
        return res
        

