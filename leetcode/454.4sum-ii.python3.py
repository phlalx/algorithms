#TAGS sum

from collections import Counter

# My first solution: O(n^3)

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        res = 0
        counter = Counter(D)
        for a in A:
            for b in B:
                for c in C:
                    res += counter[-a-b-c]
        return res

# But here's the trick, one can do two times O(n^2)

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        res = 0
        counter = Counter()
        for a in A:
            for b in B:
                counter[a+b] += 1
        for c in C:
            for d in D:
                res += counter[-c-d]
        return res
