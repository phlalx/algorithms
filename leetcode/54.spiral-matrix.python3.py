# TAGS matrix, tricky
# TODO iterative


def spiral(matrix, i, j, m, n, res):
    if m <= 0 or n <= 0:
        return
    for jj in range(j, j + n):
        res.append(matrix[i][jj])
    for ii in range(i + 1, i + m - 1):
        res.append(matrix[ii][j + n - 1])
    if m >= 2:
        for jj in reversed(range(j, j + n)):
            res.append(matrix[i + m - 1][jj])
    if n >= 2:
        for ii in reversed(range(i + 1, i + m - 1)):
            res.append(matrix[ii][j])
    spiral(matrix, i + 1, j + 1, m - 2, n - 2, res)


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if matrix:
            spiral(matrix, 0, 0, len(matrix), len(matrix[0]), res)
        return res
