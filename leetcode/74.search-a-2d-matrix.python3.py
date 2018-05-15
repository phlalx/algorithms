# TAGS sorted matrix, search
# TODO too slow... check to see the right way

import bisect


class col:
    def __init__(self, matrix, j):
        self.matrix = matrix
        self.j = j

    def __getitem__(self, i):
        return self.matrix[i][self.j]


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

        c = col(matrix, 0)

        i = bisect.bisect_left(c, target, 0, n)

        if i == n:
            i -= 1
        elif c[i] == target:
            return True
        elif i == 0:
            return False
        else:
            i -= 1

        assert 0 <= i < n

        j = bisect.bisect_left(matrix[i], target, 0, p)

        if j == p:
            return False

        return matrix[i][j] == target
