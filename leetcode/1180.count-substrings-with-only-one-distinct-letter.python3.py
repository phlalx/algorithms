        
class Solution:
    def countLetters(self, S: str) -> int:
        n = len(S)
        i = 0
        start = 0
        res = 0
        while start < n:
           
            while i < n and S[i] == S[start]:
                i += 1
            length = i - start
            res += length * (length + 1) // 2
            start = i
        return res
        



