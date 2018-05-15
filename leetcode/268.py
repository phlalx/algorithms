#TAGS xor, binary search
# Trick
# there are a few tricks
# 1. xor
# 2. binary search (if sorted array)   first i such that i >= tab[i] 
# 3. sum will overflow

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        n = len(nums) + 1
        for x in nums:
            res ^= x
        for x in range(n):
            res ^= x
        return res
        
