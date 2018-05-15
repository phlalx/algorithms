#TAGS binary search
# Redo with custom bs

from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = bisect.bisect_left(nums, target)
        j = bisect.bisect_right(nums, target)
        n = len(nums)
        if i == n or nums[i] != target:
            return [-1, -1]
        return i, j - 1
