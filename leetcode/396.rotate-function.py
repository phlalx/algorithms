
class Solution:
    def maxRotateFunction(self, A):
        s = sum(A)
        n = len(A)
        cur = sum(i * v for i, v in enumerate(A))
        res = cur
        for v in reversed(A):
            cur += s - (n * v)
            res = max(res, cur)
        return res
