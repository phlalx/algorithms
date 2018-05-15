# TAGS wiggle, quickselect
# tricky
# https://leetcode.com/problems/wiggle-sort-ii/discuss/77684/Summary-of-the-various-solutions-to-Wiggle-Sort-for-your-reference

# Explanation
#
# Notation
# odd(sol) =  [ v for i, v in enumerate(sol) if i % 2 == 1 ]
# even(sol) = [ v for i, v in enumerate(sol) if i % 2 == 1 ]
#
#  1 - if a solution exists, one can always find a solution where even <= odd
#      (we can always swap max(even) with min(odd) if needed)
#      this is the crux!
#  2 - we split the input into two groups (sorting or linear median -> see 215)
#  3 - we can almost pick even and odd groups randomly, but we need to be
#      careful with equal elements (all equal to some value v). We put v
#      elements as far apart as we can.
#  4 - TODO linear time + constant space


class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        res = [None] * n

        m = (n + 1) // 2  # even > odd

        # odd
        for k in range(m, n):
            res[2 * (k - m) + 1] = nums[m + n - 1 - k]

        # even
        for k in range(0, m):
            res[2 * k] = nums[m - 1 - k]

        nums[:] = res
