# TAGS classic, array, binary search, double pointers
#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#
# https://leetcode.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (56.49%)
# Likes:    507
# Dislikes: 921
# Total Accepted:    268.4K
# Total Submissions: 466K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
#
#
#
# Example 2:
#
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
#
#
# Note:
#
#
# Each element in the result must be unique.
# The result can be in any order.
#
#
#
#
#

# @lc code=start


# time O(n log(n))
# space O(n)

from bisect import bisect_left

def is_in(x, a):
    i = bisect_left(a,  x)
    return i < len(a) and a[i] == x

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set(nums1)
        nums2.sort()
        res = []
        for x in s:
            if is_in(x, nums2):
                res.append(x)
        return res


# time O(n log(n))
# space O(1)  (+ solution space)
# Variante merge sorte

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        n = len(nums1)
        p = len(nums2)
        res = []
        i = 0
        j = 0
        while i < n and j < p:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1
            else:
                if nums1[i] == nums2[j] and (not res or res[-1] != nums1[i]):
                    res.append(nums1[i])
                i += 1
                j += 1
        return res


# Using sets all the way

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        x = s1.intersection(s2)
        return x
# @lc code=end

