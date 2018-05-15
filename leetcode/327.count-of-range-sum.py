#
# @lc app=leetcode id=327 lang=python3
#
# [327] Count of Range Sum
#
# https://leetcode.com/problems/count-of-range-sum/description/
#
# algorithms
# Hard (33.44%)
# Likes:    456
# Dislikes: 68
# Total Accepted:    34.5K
# Total Submissions: 103.2K
# Testcase Example:  '[-2,5,-1]\n-2\n2'
#
# Given an integer array nums, return the number of range sums that lie in
# [lower, upper] inclusive.
# Range sum S(i, j) is defined as the sum of the elements in nums between
# indices i and j (i ≤ j), inclusive.
#
# Note:
# A naive algorithm of O(n^2) is trivial. You MUST do better than that.
#
# Example:
#
#
# Input: nums = [-2,5,-1], lower = -2, upper = 2,
# Output: 3
# Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective
# sums are: -2, -1, 2.
#
#
# TAGS divide and conquer
#
# 1. compute prefix sums
# 2. notice that sum(nums[a:b]) = prefix[b] - prefix[a], so we want to count
#    the number of pairs such that prefix[b] - prefix[a] is between the
#    bounds.
# 3. think divide and conquer / merger sort
# 4. count of left and right sides is recursive
# 5. count of pairs crossing the middle is in linear time (double pointer)
#
# 5 could be a cool easy problem
#

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)

        prefix = [ 0 ] * (n + 1)
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + nums[i-1]

        def count(i, j):
            m = (i + j) // 2
            count = 0
            u = m + 1
            v = m + 1
            for left in prefix[i:m+1]:
                # because left is increasing, we don't need to reset u
                # and v.
                while u <= j and prefix[u] - left < lower:
                    u += 1
                while v <= j and prefix[v] - left <= upper:
                    v += 1
                count += v - u
            return count

        def merge(i, j):
            m = (i + j) // 2
            res = []
            a = i
            b = m+1
            count = 0
            while a <= m and b <= j:
                na = prefix[a]
                nb = prefix[b]
                if na <= nb:
                    res.append(na)
                    a += 1
                else:
                    res.append(nb)
                    b += 1
            while a <= m:
                res.append(prefix[a])
                a += 1
            while b <= j:
                res.append(prefix[b])
                b += 1
            prefix[i:j+1] = res
            return count

        def f(i, j) -> int:
            # side-effect
            # sort prefix[i:j+1]
            # return count between lo and hi
            if i == j:
                return 0
            m = (i + j) // 2
            assert i <= m < m + 1 <= j
            c1 = f(i, m)
            c2 = f(m+1, j)
            c3 = count(i, j)
            merge(i, j)
            return c1 + c2 + c3

        if not nums:
            return 0

        res = f(0, len(prefix) - 1)
        return res





