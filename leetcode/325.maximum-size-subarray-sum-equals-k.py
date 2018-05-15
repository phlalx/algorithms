#TAGS 2-sum, tricky, loop invariant
# an other variant of 2-sum, I knew how to do it but it was
# hard to get it right 
#
# @lc app=leetcode id=325 lang=python3
#
# [325] Maximum Size Subarray Sum Equals k
#
# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/
#
# algorithms
# Medium (45.21%)
# Likes:    651
# Dislikes: 26
# Total Accepted:    84.2K
# Total Submissions: 186.1K
# Testcase Example:  '[1,-1,5,-2,3]\n3'
#
# Given an array nums and a target value k, find the maximum length of a
# subarray that sums to k. If there isn't one, return 0 instead.
#
# Note:
# The sum of the entire nums array is guaranteed to fit within the 32-bit
# signed integer range.
#
# Example 1:
#
#
# Input: nums = [1, -1, 5, -2, 3], k = 3
# Output: 4
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
#
#
# Example 2:
#
#
# Input: nums = [-2, -1, 2, 1], k = 1
# Output: 2
# Explanation: The subarray [-1, 2] sums to 1 and is the longest.
#
# Follow Up:
# Can you do it in O(n) time?
#

# 0   cur = 0
#     sum = {}

#     cur = a[0]
#     sum = {}
# 1
#     cur = a[0]
#     sum = {}

#     sum = { a[0] }
#     cur = a[1]
# 2
#     cur = a[1]
#     sum = { a[0] }

#     sum = { a[0], a[1] }
#     cur = a[2]
# 3
#     sum = { a[1]}
#     cur = a[2]


#     sum = { a[0], a[1]}
#     cur = a[3]


# start with invariant we want in the loop, everything
# else follow from this
#
# It is simpler to define s[i] = sum(nums[:i])
# We can define it explicitely (solution 1), or use it as a
# definition to express the invariants (solution 2)
#

# Solution 1
class Solution:
    def maxSubArrayLen(self, nums, k):
        if not nums:
            return 0

        n = len(nums)
        s = [0] * (n+1)
        for i in range(1, n+1):
            s[i] = s[i-1] + nums[i-1]
        seen = {0:0}
        best = 0
        for i in range(1, n+1):
            # invariant
            # seen = { s[j] : j for j < i }
            v = s[i]
            j = seen.get(v - k)
            if j is not None and i - j > best:
                # the first solution we find may not be the
                # best one
                best = i - j
            seen.setdefault(v, i)

        return best

# Solution 2
class Solution:
    def maxSubArrayLen(self, nums, k):
        if not nums:
            return 0
        n = len(nums)
        seen = {0:0}
        best = 0
        v = 0
        for i in range(1, n+1):
            # invariant
            # v = s[i-1]
            # seen = { s[j] : j for j <= i-1 }
            v += nums[i-1]
            j = seen.get(v - k)
            if j is not None and i - j > best:
                best = i - j
            seen.setdefault(v, i)
        return best

def test():
    s = Solution().maxSubArrayLen([0, 0], 0)
    print(s)

test()
