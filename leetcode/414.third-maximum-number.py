#TAGS array

# Priority queue isn't working here. Because the complexity isn't right,
# and we'd need to deduplicate the elements.
#

def push(arr, v):
    if v in arr:
        return
    if v > arr[2]:
        arr[0], arr[1] = arr[1], arr[2]
        arr[2] = v
    elif v > arr[1]:
        arr[0] = arr[1]
        arr[1] = v
    elif v > arr[0]:
        arr[0] = v

class Solution:
    def thirdMax(self, nums):
        # we keep a sorted array of three elements
        arr = [float('-inf')] * 3
        for v in nums:
            push(arr, v)
        if arr[0] == float('-inf'):
            return arr[2]
        return next(x for x in arr if x != float('-inf'))

