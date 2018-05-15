from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        counter = Counter(nums)

        for v in nums:
            if counter[v] == 0:
                continue
            for i in range(k):
                if counter[v + i] == 0:
                    return False
                counter[v+i] -= 1

        return True

        
