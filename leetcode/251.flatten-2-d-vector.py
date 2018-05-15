# TAGS iterator, cool, classic
#
# @lc app=leetcode id=251 lang=python3
#
# [251] Flatten 2D Vector
#
# https://leetcode.com/problems/flatten-2d-vector/description/
#
# algorithms
# Medium (44.46%)
# Likes:    268
# Dislikes: 138
# Total Accepted:    63K
# Total Submissions: 141.5K
# Testcase Example:  '["Vector2D","next","next","next","hasNext","hasNext","next","hasNext"]\n' +
#
# Design and implement an iterator to flatten a 2d vector. It should support
# the following operations: next and hasNext.
#
#
#
# Example:
#
#
# Vector2D iterator = new Vector2D([[1,2],[3],[4]]);
#
# iterator.next(); // return 1
# iterator.next(); // return 2
# iterator.next(); // return 3
# iterator.hasNext(); // return true
# iterator.hasNext(); // return true
# iterator.next(); // return 4
# iterator.hasNext(); // return false
#
#
#
#
# Notes:
#
#
# Please remember to RESET your class variables declared in Vector2D, as
# static/class variables are persisted across multiple test cases. Please see
# here for more details.
# You may assume that next() call will always be valid, that is, there will be
# at least a next element in the 2d vector when next() is called.
#
#
#
#
# Follow up:
#
# As an added challenge, try to code it using only iterators in C++ or
# iterators in Java.
#
#

# Solution 1
# invariant: i,j is where it should be when calling next
# next_valid adjust (i, j) if need to
# We place (i, j) after next (and in the constructor), then has_next is just
# a test
# The other option would be to replace (i, j) before calling next.
class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.v = v
        self.i = 0
        self.j = 0
        self.n = len(v)
        self._next_valid()

    def next(self) -> int:
        res = self.v[self.i][self.j]
        self.j += 1
        self._next_valid()
        return res

    def hasNext(self) -> bool:
        return self.i != self.n

    def _next_valid(s):
        while s.i < s.n and not (s.j < len(s.v[s.i])):
            s.j = 0
            s.i += 1

# Solution 2
# invariant: i,j is where we left it at the last call
# We adjust it before calling next, and before calling has next
# I prefer solution 1, I find the invariant easier to reason about.
# hasNext is just a test, and next start with a simple access.
# But we need extra work in the constructor
class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.v = v
        self.i = 0
        self.j = 0
        self.n = len(v)

    def next(self) -> int:
        self._next_valid()
        res = self.v[self.i][self.j]
        self.j += 1
        return res

    def hasNext(self) -> bool:
        self._next_valid()
        return self.i != self.n

    def _next_valid(s):
        while s.i < s.n and not (s.j < len(s.v[s.i])):
            s.j = 0
            s.i += 1

# Solution 3, using iterators
# Problem: python iterators don't have hasNext method.
#          we compute the next element in advance
#          looks similar to Solution 1
class Vector2D:

    def __init__(self, v: List[List[int]]):
        # suppose i'm given an iterator of iterators
        x = [iter(l) for l in v]
        self.v = iter(x)

        self.cur_line = next(self.v, None)
        self._next_valid()

    def next(self) -> int:
        res = self.next_elt
        self._next_valid()
        return res

    def hasNext(self) -> bool:
        return self.next_elt is not None

    # update next element, and consume iterators
    def _next_valid(self):
        self.next_elt = None
        while self.cur_line is not None:
            elt = next(self.cur_line, None)
            if elt is not None:
                self.next_elt = elt
                break
            self.cur_line = next(self.v, None)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()

