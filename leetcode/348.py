#TAGS easy, data structure

class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag1 = 0
        self.diag2 = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        player_ = 1 if player == 1 else -1
        self.rows[row] += player_
        self.cols[col] += player_
        if row == col:
          self.diag1 += player_
        if col == self.n - 1 - row:  
          self.diag2 += player_
        winning_cond = self.n * player_
        if winning_cond in {self.rows[row], self.cols[col], self.diag1, self.diag2}:
          return player
        return 0
        
