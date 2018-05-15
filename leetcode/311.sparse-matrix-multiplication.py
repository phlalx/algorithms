#TAGS matrices

def matrix_to_lines(A):
    n = len(A)
    p = len(A[0])
    res = []
    for i in range(n):
        line = []
        for j in range(p):
            line.append((j, A[i][j]))
        if line:
            res.append((i, line))
    return res

def matrix_to_columns(B):
    n = len(B)
    p = len(B[0])
    B = [[B[j][i] for j in range(n)] for i in range(p)]
    return matrix_to_lines(B)

def prod(l, r):
    i = 0
    j = 0
    res = 0
    while i < len(l) and j < len(r):
        a, v = l[i]
        b, w = r[j]
        if a == b:
            res += v * w
            i += 1
            j += 1
        elif a < b:
            i += 1
        else:
            j += 1
    return res

class Solution:
    def multiply(self, A, B):
        lines_A = matrix_to_lines(A)
        cols_B = matrix_to_columns(B)
        n = len(A)
        r = len(B[0])
        res = [[ 0 for _ in range(r)] for _ in range(n) ]
        for i, line in lines_A:
            for j, col in cols_B:
                res[i][j] = prod(line, col)
        return res
