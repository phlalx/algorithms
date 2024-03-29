#
# @lc app=leetcode id=1130 lang=python3
#
# [1130] Minimum Cost Tree From Leaf Values
#
# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/description/
#
# algorithms
# Medium (65.41%)
# Likes:    980
# Dislikes: 83
# Total Accepted:    28.6K
# Total Submissions: 43.7K
# Testcase Example:  '[6,2,4]'
#
# Given an array arr of positive integers, consider all binary trees such
# that:
#
#
# Each node has either 0 or 2 children;
# The values of arr correspond to the values of each leaf in an in-order
# traversal of the tree.  (Recall that a node is a leaf if and only if it has 0
# children.)
# The value of each non-leaf node is equal to the product of the largest leaf
# value in its left and right subtree respectively.
#
#
# Among all possible binary trees considered, return the smallest possible sum
# of the values of each non-leaf node.  It is guaranteed this sum fits into a
# 32-bit integer.
#
#
# Example 1:
#
#
# Input: arr = [6,2,4]
# Output: 32
# Explanation:
# There are two possible trees.  The first has non-leaf node sum 36, and the
# second has non-leaf node sum 32.
#
# ⁠   24            24
# ⁠  /  \          /  \
# ⁠ 12   4        6    8
# ⁠/  \               / \
# 6    2             2   4
#
#
#
# Constraints:
#
#
# 2 <= arr.length <= 40
# 1 <= arr[i] <= 15
# It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is
# less than 2^31).
#
#
# TAGS dp
# @lc code=start
import functools
from typing import Tuple

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        @functools.lru_cache(maxsize=None)
        def f(i, j) -> Tuple[int, int]:
            if i == j:
                return 0, arr[i]
            else:
                res = float('inf'), None
                for k in range(i, j):
                    u, v = f(i, k)
                    uu, vv = f(k+1, j)
                    res = min(res, (u + uu + v * vv, max(v, vv)))
                return res

        return f(0, n-1)[0]


# @lc code=end

