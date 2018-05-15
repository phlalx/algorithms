#TAGS dp, kadane
# variant of kadane

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = 1
        cur_min = 1
        res = float('-inf')
        for v in nums:
            cur_max, cur_min = max(v * cur_max, v * cur_min, v), min(v * cur_max, v * cur_min, v)
            res = max(cur_max, res)
        return res
