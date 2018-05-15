#TAGS parenthesis greedy

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        count = 0
        res = 0
        for c in S:
            if c == '(':
                count += 1
            elif count > 0:
                count -= 1
            else:
                res += 1
        return res + count
        
