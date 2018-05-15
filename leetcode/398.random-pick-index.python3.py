# TAGS list, binary search
#
# Solution 1
#   . sort while keeping indexes (done once)
#   . using binary search find bounds of target (O(log(n)))
#   . pick random number in this range
#

import bisect
import random


class Wrapper:  # pythonic
    def __init__(self, nums):
        self.nums = nums

    def __getitem__(self, i):
        return self.nums[i][1]


class Solution:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = list(enumerate(nums))
        self.nums.sort(key=lambda x: x[1])

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        n = len(self.nums)
        f = Wrapper(self.nums)
        left = bisect.bisect_left(f, target, 0, n)
        right = bisect.bisect_right(f, target, 0, n)
        i, _ = self.nums[random.randrange(left, right)]
        return i


# Solution 2 (easy)
#
# from collections import defaultdict
# from random import choice
#
# class Solution:
#
#  def __init__(self, l):
#    self.d = defaultdict(list)
#    for i, v in enumerate(l):
#      self.d[v].append(i)
#
#  def pick(self, target):
#    return choice(self.d[target])
#

# test()

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
