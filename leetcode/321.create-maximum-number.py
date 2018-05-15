#
# @lc app=leetcode id=321 lang=python3
#
# [321] Create Maximum Number
#
# https://leetcode.com/problems/create-maximum-number/description/
#
# algorithms
# Hard (25.82%)
# Likes:    582
# Dislikes: 203
# Total Accepted:    36.7K
# Total Submissions: 138.4K
# Testcase Example:  '[3,4,6,5]\n[9,1,2,5,8,3]\n5'
#
# Given two arrays of length m and n with digits 0-9 representing two numbers.
# Create the maximum number of length k <= m + n from digits of the two. The
# relative order of the digits from the same array must be preserved. Return an
# array of the k digits.
#
# Note: You should try to optimize your time and space complexity.
#
# Example 1:
#
#
# Input:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# Output:
# [9, 8, 6, 5, 3]
#
# Example 2:
#
#
# Input:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# Output:
# [6, 7, 6, 0, 4]
#
# Example 3:
#
#
# Input:
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
# Output:
# [9, 8, 9]
#
#

# @lc code=start

# TAGS cool, monotonic stack
#
#   See 503  for getMaxNumber
#
#   Common reasoning pattern:
#   if S is a solution, so S is a combination of Left and Right, where Left
#   is a solution of nums1 for some i, and Right is a solution of nums2 for some
#   j where i + j == n
#
#   So we find the solutions to the sub-problems  and combine them to get the
#   best solution overall.
#
#   building block 402
#
# See for instance https://leetcode.com/problems/create-maximum-number/discuss/77291/Share-my-Python-solution-with-explanation
#
def removeKdigits(num: str, k: int) -> str:
    res = []
    len_res = len(num) - k
    for v in num:
        while res and res[-1] < v and k:
            res.pop()
            k -= 1
        res.append(v)
    res = res[:len_res]
    return res

def keepKdigits(nums, k):
    return removeKdigits(nums, len(nums) - k)

def merge(a1, a2):
    # this is not a merge sort
    res = []
    while a1 or a2:  # TODO undertsand this strange condition
        if a1 >= a2:
            res.append(a1.pop(0))
        else:
            res.append(a2.pop(0))
    res.extend(a1)
    res.extend(a2)
    return res

class Solution:
    def maxNumber(self, nums1, nums2, k):
        res = []
        # This took me more time than it should... just solve the inequalities
        # 0 <= i <= n1
        # 0 <= k - i <= n2
        # ...
        for i in range(max(0, k-len(nums2)), min(k, len(nums1)) + 1):
            a1 = keepKdigits(nums1, i)
            a2 = keepKdigits(nums2, k - i)
            m = merge(a1, a2)
            res = max(res, m)
        return res

# @lc code=end

