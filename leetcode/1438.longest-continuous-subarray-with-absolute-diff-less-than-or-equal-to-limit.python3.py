#TAGS monotonic stack, sliding window, classic, cool

#Take away:
#  - maintain two monotonic stack, one for min, one for max
#  - outer loop is on j (easier to maintain window) 
#
# There are other solutions
#  - use a bst
#  - use 2-heaps (keep min/max, and lazy removal)  TODO
#
#

from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        i = 0
        res = 0
        incr = deque()
        decr = deque()
        for j, v in enumerate(nums):
 
            while incr and v <= nums[incr[-1]]:
                incr.pop()
            incr.append(j)
            while decr and v >= nums[decr[-1]]:
                decr.pop()
            decr.append(j)

            while (nums[decr[0]] - nums[incr[0]]) > limit:
                if decr[0] == i:
                    decr.popleft()
                if incr[0] == i:
                    incr.popleft()    
                i += 1 
                
            res = max(res, j - i + 1)
        return res
            
