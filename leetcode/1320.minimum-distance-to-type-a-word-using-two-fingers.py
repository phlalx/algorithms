#TAGS dp
#
# Quite simple, but need to be careful with the implementation
# DP is 2d, but it could be 1d and constant space
# REDO

from string import ascii_uppercase

ROWSIZE = 6

class Solution:
    def minimumDistance(self, word: str) -> int: 
        n = len(word)
        m = {}
      
        for c in ascii_uppercase:
            offset = ord(c) - ord('A')
            i, j = divmod(offset, ROWSIZE)
            m[c] = i, j
        
        def d(i, j):
            # trick: only consider indices of letter, no need to compute distance
            # between arbitrary letters or positions
            # this makes the dp function easier
            if i == -1 or j == -1:
                return 0
            return sum(abs(m[word[i]][u] - m[word[j]][u]) for u in range(2))
    
        # i = first index that remains to be typed
        # one finger is on i - 1
        # other finger is on j
        memo = {}
        def f(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == n:
                res = 0
            else:
                res = min(d(i-1, i) + f(i+1, j), d(j, i) + f(i+1, i-1))
            memo[(i, j)] = res
            return res
        
        return f(0, -1)
             
