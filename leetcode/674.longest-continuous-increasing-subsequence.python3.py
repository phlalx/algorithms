#TAGS array
# Just maintain a counter of the longest current continuous subsequence
# See also 300

def lcis(nums):
    cur = 1
    best = 1
    prev = nums[0]
    for i in nums[1:]:
        if i > prev:
            cur = cur + 1
            best = max(cur, best)
        else:
            cur = 1
        prev = i
    return best


class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            return lcis(nums)
        else:
            return 0
