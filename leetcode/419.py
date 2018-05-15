#TAGS grid
#TRICK don't do dfs, instead count every top-left squares
#  this wouldn't work for islands

from itertools import product

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0
        
        n = len(board)
        p = len(board[0])
    
        res = 0
        for i, j in product(range(n), range(p)):
            if (board[i][j] == '.' or (i > 0 and board[i-1][j] == 'X') or j > 0 and board[i][j-1] == 'X') :
                continue
            res += 1


        return res
            
    
