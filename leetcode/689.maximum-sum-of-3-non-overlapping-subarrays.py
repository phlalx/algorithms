#
# @lc app=leetcode id=689 lang=python3
#
# [689] Maximum Sum of 3 Non-Overlapping Subarrays
#
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description/
#
# algorithms
# Hard (45.75%)
# Likes:    887
# Dislikes: 53
# Total Accepted:    39.6K
# Total Submissions: 86.4K
# Testcase Example:  '[1,2,1,2,6,7,5,1]\n2'
#
# In a given array nums of positive integers, find three non-overlapping
# subarrays with maximum sum.
#
# Each subarray will be of size k, and we want to maximize the sum of all 3*k
# entries.
#
# Return the result as a list of indices representing the starting position of
# each interval (0-indexed). If there are multiple answers, return the
# lexicographically smallest one.
#
# Example:
#
#
# Input: [1,2,1,2,6,7,5,1], 2
# Output: [0, 3, 5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting
# indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be
# lexicographically larger.
#
#
#
#
# Note:
#
#
# nums.length will be between 1 and 20000.
# nums[i] will be between 1 and 65535.
# k will be between 1 and floor(nums.length / 3).
#
#
#
#
#

# TAGS dp, classic
# TODO iterative
# TODO check other solutions

# @lc code=start
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # define accumulator, usual in summing problems
        # acc[i+k] - acc[i] = nums[i:i+k]
        acc = [0]
        for v in nums:
            acc.append(v + acc[-1])

        #
        # 1. restate the problem in term of acc
        #
        # find a_i such that
        # max(acc[a_i+k] - acc[a_i]) is maximal
        # a_0 >= 0
        # a_0 + k <= a1
        # a_1 + k <= a2
        # a_2 + k <= n
        #
        # The bounds of the problem don't change. The only thing that
        # changes is that we can replace sum(num[i:j]) with acc[j] - acc[i]
        #
        memo = {}
        def f(i, v):
            if (i, v) in memo:
                return memo[(i,v)]
            if v == 0:
                res = 0, ()
            elif i + k > n:
                res = float('-inf'), ()
            else:
                # I initially made a mistake here, I tried all the possible
                # i, but it's enough to either skip i, or call f(i+1, ...)
                a, sol_a = f(i+1, v)
                b, sol_b = f(i+k, v-1)
                diff = acc[i+k] - acc[i]
                if diff + b >= a:
                    res = (diff + b), ((i,) + sol_b)
                else:
                    res = a, sol_a
            memo[(i,v)] = res
            return res

        return f(0, 3)[1]

# TODO quite simple!
#
# There is a simple O(n) O(1) solution
# Keep 3 sliding windows sliding together (and touching each other)
#   XXXX|A|B|C|XXXX
#
#  We maintain three variables
#    best  A
#    best  A + B
#    best  A + B + C
#


