#
# @lc app=leetcode id=668 lang=python3
#
# [668] Kth Smallest Number in Multiplication Table
#
# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/description/
#
# algorithms
# Hard (45.08%)
# Likes:    490
# Dislikes: 20
# Total Accepted:    19.9K
# Total Submissions: 43.9K
# Testcase Example:  '3\n3\n5'
#
#
# Nearly every one have used the Multiplication Table. But could you find out
# the k-th smallest number quickly from the multiplication table?
#
#
#
# Given the height m and the length n of a m * n Multiplication Table, and a
# positive integer k, you need to return the k-th smallest number in this
# table.
#
#
# Example 1:
#
# Input: m = 3, n = 3, k = 5
# Output:
# Explanation:
# The Multiplication Table:
# 1    2    3
# 2    4    6
# 3    6    9
#
# The 5-th smallest number is 3 (1, 2, 2, 3, 3).
#
#
#
#
# Example 2:
#
# Input: m = 2, n = 3, k = 6
# Output:
# Explanation:
# The Multiplication Table:
# 1    2    3
# 2    4    6
#
# The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
#
#
#
#
# Note:
#
# The m and n will be in the range [1, 30000].
# The k will be in the range [1, m * n]
#
#
#
#TAGS binary search
# trick: binary search the answer
# see also 378, 719
#
# Once we get the idea, two tricky things remain (see code)
#

# @lc code=start

# returns smallest x such that p[x] is True
# else j + 1
def binary_search(i, j, pred):
    while i < j:
        m = (i + j) // 2
        assert i <= m < m + 1 <= j
        # mental model: [i,m] larger by at most one of [m+1,j]
        # each part is stricly smaller than [i, j]
        # no risk of infinite loop here, as long as we stop the loop
        # when i == j
        # - - - + + +
        # - - - - + +
        if pred(m):
            j = m
        else:
            i = m + 1
    return i if pred(i) else i + 1


# trick 1: took me more time than needed
def count(n, p, v):
    # num of elements no larger than v
    res = 0
    for i in range(1, n+1):
        res += min(v // i, p)
    return res

# trick 2: understand how to "invert" the count fonction
#
# suppose we have this array
# [1,1,2,2,3]
#
# `__item__` is not bijective. Each rank has an element, but two identical
# elements can have different ranks. It doesn't make sense to ask
# "what is the rank of 2"?
#
# Here we have access to the function `count` that returns the number of
# elements no larger than some `v`.
#
# count:
# elt -> count
#  1 -> 1
#  2 -> 2
#  3 -> 5
#
# From there we can deduce the kth-element
#
# TODO: need to grok this better
#




class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        pred = lambda v: count(m, n, v) >= k
        return binary_search(1, m*n, pred)


# @lc code=end

