# TAGS matrix, classic
#
# O(n + p)
# consider the square
# u ---- v
# |      |
# x -----y
#
# we can remove a line and a col at each iteration, we compare target
# to x and v.
#
# See cracking the coding interview for better complexity


def search(m, i, j, ii, jj, v):
    if not (i <= ii and j <= jj):
        return False
    if v in {m[i][j], m[ii][j], m[i][jj], m[ii][jj]}:
        return True
    if v < m[i][j] or v > m[ii][jj]:
        return False
    a = v < m[i][jj]
    b = v < m[ii][j]
    if a:
        jj = jj - 1
    else:
        i = i + 1
    if b:
        ii = ii - 1
    else:
        j = j + 1
    return search(m, i, j, ii, jj, v)


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        n = len(matrix)
        p = len(matrix[0])
        return search(matrix, 0, 0, n - 1, p - 1, target)
