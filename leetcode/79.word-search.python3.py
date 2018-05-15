# TAGS grid, complete search, backtrack

s = list(zip([0, 1, 0, -1], [1, 0, -1, 0]))


def succ(a, b, m, n):
    return ((a + x, b + y) for (x, y) in s if 0 <= a + x < m and 0 <= b + y < n)


def walk(board, word, i, j, i_word):
    c = board[i][j]
    if c != word[i_word]:
        return False
    if i_word == len(word) - 1:
        return True
    for u, v in succ(i, j, len(board), len(board[0])):
        if board[u][v] == "*":
            continue
        c = board[i][j]
        board[i][j] = "*"
        if walk(board, word, u, v, i_word + 1):
            return True
        board[i][j] = c
    return False


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)  # lines
        n = len(board[0])  # col
        return any(walk(board, word, i, j, 0) for i in range(m) for j in range(n))
