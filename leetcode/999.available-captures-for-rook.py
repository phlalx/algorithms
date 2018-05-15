#
# @lc app=leetcode id=999 lang=python3
#
# [999] Available Captures for Rook
#
# https://leetcode.com/problems/available-captures-for-rook/description/
#
# algorithms
# Easy (65.85%)
# Likes:    138
# Dislikes: 306
# Total Accepted:    21.9K
# Total Submissions: 33.3K
# Testcase Example:  '[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]'
#
# On an 8 x 8 chessboard, there is one white rook.  There also may be empty
# squares, white bishops, and black pawns.  These are given as characters 'R',
# '.', 'B', and 'p' respectively. Uppercase characters represent white pieces,
# and lowercase characters represent black pieces.
# 
# The rook moves as in the rules of Chess: it chooses one of four cardinal
# directions (north, east, west, and south), then moves in that direction until
# it chooses to stop, reaches the edge of the board, or captures an opposite
# colored pawn by moving to the same square it occupies.  Also, rooks cannot
# move into the same square as other friendly bishops.
# 
# Return the number of pawns the rook can capture in one move.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input:
# [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 3
# Explanation: 
# In this example the rook is able to capture all the pawns.
# 
# 
# Example 2:
# 
# 
# 
# 
# Input:
# [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 0
# Explanation: 
# Bishops are blocking the rook to capture any pawn.
# 
# 
# Example 3:
# 
# 
# 
# 
# Input:
# [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 3
# Explanation: 
# The rook can capture the pawns at positions b5, d6 and f5.
# 
# 
# 
# 
# Note:
# 
# 
# board.length == board[i].length == 8
# board[i][j] is either 'R', '.', 'B', or 'p'
# There is exactly one cell with board[i][j] == 'R'
# 
# 
#

# TAGS pythonic

# @lc code=start
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0
        n = len(board)
        p = len(board[0])
        in_grid = lambda x, y: 0 <= x < n and 0 <= y < p
        i, j = next( (i, j) for i in range(n) for j in range(p) if board[i][j] == 'R'  )
        res = 0
        for (a, b) in zip([0,1,0,-1], [1,0,-1,0]):
            ii, jj = (i + a, j + b)
            while in_grid(ii, jj) and board[ii][jj] == '.':
                ii, jj = ii + a, jj + b
            if in_grid(ii, jj) and board[ii][jj]  == 'p':
                res += 1
        return res
# @lc code=end

