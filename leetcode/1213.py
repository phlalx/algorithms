#TAGS merge
# easy

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        n = len(arr1)
        p = len(arr2)
        q = len(arr3)
        i = 0
        j = 0
        k = 0
        res = []
        while i < n and j < p and k < q:
            if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
                res.append(arr1[i])
                i += 1
                j += 1
                k += 1
            elif arr1[i] <= min(arr2[j], arr3[k]):
                i += 1
            elif arr2[j] <min(arr1[i], arr3[k]):
                j += 1
            else:
                k += 1
        return res
