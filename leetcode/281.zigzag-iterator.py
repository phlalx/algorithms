#
# @lc app=leetcode id=281 lang=python3
#
# [281] Zigzag Iterator
#
# https://leetcode.com/problems/zigzag-iterator/description/
#
# algorithms
# Medium (58.16%)
# Likes:    368
# Dislikes: 20
# Total Accepted:    63.5K
# Total Submissions: 109.1K
# Testcase Example:  '[1,2]\n[3,4,5,6]'
#
# Given two 1d vectors, implement an iterator to return their elements
# alternately.
#
#
#
# Example:
#
#
# Input:
# v1 = [1,2]
# v2 = [3,4,5,6]
# Output: [1,3,2,4,5,6]
# Explanation: By calling next repeatedly until hasNext returns false, the
# order of elements returned by next should be: [1,3,2,4,5,6].
#
#
#
# Follow up:
#
# What if you are given k 1d vectors? How well can your code be extended to
# such cases?
#
# Clarification for the follow up question:
# The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases.
# If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For
# example:
#
#
# Input:
# [1,2,3]
# [4,5,6,7]
# [8,9]
#
# Output: [1,4,8,2,5,9,3,6,7].
#
#
#



# @lc code=start
#TAGS data structure, easy

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.i = 0
        self.j = 0
        self.n = len(v1)
        self.p = len(v2)
        self.v1 = v1
        self.v2 = v2
        self.is_next_v1 = bool(self.n)

    def next(self) -> int:
        if self.is_next_v1:
            self.i += 1
            if self.j < self.p:
                self.is_next_v1 = False
            return  self.v1[self.i - 1]
        else:
            self.j += 1
            if self.i < self.n:
                self.is_next_v1 = True
            return  self.v2[self.j - 1]


    def hasNext(self) -> bool:
        return self.i < self.n or self.j < self.p


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

