# TAGS string
# TODO slow


def count_bits(nums):
    bit_count = [0] * 32
    for n in nums:
        b = reversed(bin(n)[2:])
        for i, v in enumerate(b):
            bit_count[i] += int(v)
    n = len(nums)
    return sum(b * (n - b) for b in bit_count)


class Solution:
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return count_bits(nums)


def test():
    sol = Solution()
    assert sol.totalHammingDistance([4, 12, 4]) == 2
    assert sol.totalHammingDistance([1, 2]) == 2


test()
