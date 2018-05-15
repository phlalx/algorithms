# TAGS grid
# TODO use sliding window?


class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n = len(board)
        p = len(board[0])

        def get(i, j):
            if 0 <= i < n:
                if 0 <= j < p:
                    return board[i][j]
            return 0

        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]

        def num_neighbors(i, j):
            return sum(get(i + a, j + b) for a, b in dirs)

        kill = []
        born = []

        for i in range(n):
            for j in range(p):
                nn = num_neighbors(i, j)
                if board[i][j] and (nn <= 1 or nn >= 4):
                    kill.append((i, j))
                elif not board[i][j] and nn == 3:
                    born.append((i, j))

        for i, j in kill:
            board[i][j] = 0

        for i, j in born:
            board[i][j] = 1
