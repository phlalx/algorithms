#
# @lc app=leetcode id=650 lang=python3
#
# [650] 2 Keys Keyboard
#
# https://leetcode.com/problems/2-keys-keyboard/description/
#
# algorithms
# Medium (47.15%)
# Likes:    772
# Dislikes: 53
# Total Accepted:    39.7K
# Total Submissions: 83.8K
# Testcase Example:  '3'
#
# Initially on a notepad only one character 'A' is present. You can perform two
# operations on this notepad for each step:
#
#
# Copy All: You can copy all the characters present on the notepad (partial
# copy is not allowed).
# Paste: You can paste the characters which are copied last time.
#
#
#
#
# Given a number n. You have to get exactly n 'A' on the notepad by performing
# the minimum number of steps permitted. Output the minimum number of steps to
# get n 'A'.
#
# Example 1:
#
#
# Input: 3
# Output: 3
# Explanation:
# Intitally, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.
#
#
#
#
# Note:
#
#
# The n will be in the range [1, 1000].
#
#
#
#
#

# @lc code=start
class Solution:
    def minSteps(self, n: int) -> int:
        memo = {}
        def f(a, b):
            if a == n:
                return 0
            res = memo.get((a, b))
            if res is not None:
                return res
            res = float('inf')
            if a != b:
                res = min(res, 1 + f(a, a))
            if a + b  <= n and  b != 0:
                res = min(res, 1 + f(a+b, b))
            memo[(a,b)] = res
            return res
        return  f(1,0)

# @lc code=start

from collections import deque

class Solution:
    def minSteps(self, n: int) -> int:
        dq = deque()
        dq.append((1,0))
        seen = {}
        seen[(1, 0)] = 0
        while dq:
            a, b = dq.popleft()
            dist = seen[(a, b)]
            if a == n:
                return dist
            if a + b <=n and (a+b, b) not in seen:
                seen[(a+b, b)] = dist + 1
                dq.append((a+b,b))
            if (a, a) not in seen:
                seen[(a, a)] = dist + 1
                dq.append((a,a))
        assert 0

# @lc code=end

