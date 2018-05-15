#TAGS intervals, merge sort, cool

class Solution:
    def intervalIntersection(self, A, B):
        n = len(A)
        p = len(B)
        res = []
        i = 0
        j = 0
        while i < n and j < p:
            u, v = A[i]
            a, b = B[j]
            if u <= a:
                if b <= v:
                    res.append([a, b])
                    j += 1
                elif a <= v:
                    res.append([a, v])
                    i += 1
                else:
                    i += 1
            else:
                A, B, i, j, n, p = B, A, j, i, p, n
        return res


