# TAGS traversal, matrix


class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        if n == 0:
            return []
        m = len(matrix[0])
        if m == 0:
            return []
        res = []
        up = False
        # for each diagonal, i + j = k
        for k in range(n + m - 1):
            i_first = max(0, k - (m - 1))
            i_last = min(k, n - 1)
            # print(k, i_first, i_last)
            r = range(i_first, i_last + 1)
            if not up:
                r = reversed(r)
            for i in r:
                res.append(matrix[i][k - i])
            up = not up
        return res
