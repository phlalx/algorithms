# TAGS permutation
# node: elements can be repeated
# trick:
#  think regular ordering
#   1299, 1300, 1399, 1400
#  difference here is that
#    first is sorted    1 2 3 4
#    last  is reversed  4 3 2 1
#
#  we want to keep the longest possible prefix invariant
#  consider the longest decreasing suffix, there is no way to make it bigger
#  example 1 2 | 5 4 3
#  we take the smallest number in the suffix just above the last of the prefix,
#  replace it with the last number of the prefix, and sort the suffix
#   not that sort here is just reversing
#
#  1 2 | 5 4 3
#  1 3 | 5 4 2
#  1 3 | 2 4 5


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2

        # find the longest reverse-sorted suffix
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # nums[i+1:] is reversed sorted
        if i == -1:
            # nums is sorted in reverse order
            nums.reverse()
            return

        # these two lines could be done in place and in one iteration
        nums[i + 1 :] = reversed(nums[i + 1 :])
        j = next(j + i + 1 for j, a in enumerate(nums[i + 1 :]) if a > nums[i])
        nums[i], nums[j] = nums[j], nums[i]


def test():
    s = Solution()
    nums = [1, 3, 2]
    print(nums)
    while True:
        s.nextPermutation(nums)
        print(nums)
        input()


# test()
