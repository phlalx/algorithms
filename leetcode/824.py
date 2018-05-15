#TAGS string
# stupid

def f(w, i):
    if w[0] in 'aeiouAEIOU':
        res = w
    else:
        res = w[1:] + w[0]
    return res + 'ma' + (i + 1) * 'a'
    

class Solution:
    def toGoatLatin(self, S: str) -> str:
        res = []
        for i, w in enumerate(S.split()):
            res.append(f(w, i))
        return ' '.join(res)
            
            
        
