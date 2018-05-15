#TAGS classic, cool, sliding window, monotonic stack
#
# Sliding window problems usually consists of computing a function
# f(a, b) for a set of windows [a:b].
#
# The trick is to find a relation of the form f(a, b) = F(f(a', b')) where
# [a':b'] is the window seen right before.
#
# For instance f(a, b) = F(f(a-1, b-1), b) (we can use the new value).
#
# In this case, f(a, b) = max(l[a:b]). There is no function F that will work
# for this definition of f.
#
# What we can do is find a function g(a, b) that computes some structure
# from which we can derive f, and such that we can easily compute g
# recursively.
#
# Back to this problem. We look for a function g. It should returns some
# abstraction of the window, from which we can easily compute what we want
# and that we can update in constant time when the window advances.
#
# Suppose the current window contains [1, 2, 4, 3]. We can forget 1 and 2,
# they will never become the new max. However, 3 may become the max when
# 4 is pushed out ==> monotonic stack.
#
# But when to evict stuff from the stack?
#
# Tentative, when the stack is full, but no...
#
# 1 3 1 2 0 5
# -----
# 3 1
#   -----
#   3 2
#     -----
#     3 2 0 (Aie!)
#       -----
#       5
# 3 3 3 5
#
# We need to keep the index of the element

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        n = len(nums)

        def ms_push(d, i):
            if d and i - d[0][1] >= k:
                d.popleft()
            v = nums[i]
            while d and v >= d[-1][0]:
                d.pop()
            d.append((v, i))

        def ms_max(d):
            return d[0][0]

        res = []
        d = deque()
        for i in range(0, k-1):
            ms_push(d, i)
        i = 0
        while i + k <= n:
            # consider window [i:i+k]
            # forget i - 1
            # welcome i + k - 1
            ms_push(d, i+k-1)
            m = ms_max(d)
            res.append(m)
            i += 1
        return res
