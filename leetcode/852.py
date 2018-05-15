#TAGS binary search

# return smallest k such that pred[k] for k in [i..j]
#        j + 1 no such k
def binary(pred, i, j):
    while i < j:
        m = (i + j) // 2
        if pred(m):
            j = m
        else:
            i = m + 1
    return i

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        pred = lambda i: arr[i] >= arr[i+1]
        return binary(pred, 0, len(arr) - 2)
        
