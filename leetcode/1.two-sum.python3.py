# TAGS array, double pointer, classic
#
# This is at the basis of a lot of problems
#

# think looking up in ordered matrix Mij = Ai + Bj
# By case on the top-right corner
#
def two_sum_in_place(nums, target):
    sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
    i = 0
    j = len(nums) - 1
    while i < j:
        two_sum = sorted_nums[i][1] + sorted_nums[j][1]
        if two_sum == target:
            return [sorted_nums[i][0], sorted_nums[j][0]]
        elif two_sum < target:
            i += 1
        else:
            j -= 1
    assert False


def two_sum_linear(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        j = seen.get(target - num)
        if j is not None:
            return [i, j]
        seen[num] = i
    assert False


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return two_sum_linear(nums, target)
