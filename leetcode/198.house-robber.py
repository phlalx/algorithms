#TAGS dp

class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        prev = 0
        cur = nums[0]
        for v in nums[1:]:
            cur, prev = max(v + prev, cur), cur
        return cur
