
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        key = {}
  
        for i, a in enumerate(order):
            key[a] = i
    
        def smaller(w, ww):
            for a, b in zip(w, ww):
                if key[a] < key[b]:
                    return True
                elif key[a] > key[b]:
                    return False
            return len(w) <= len(ww)
  
        for w, ww in zip(words, words[1:]):
            if not smaller(w, ww):
                return False
        return True 


# simpler but using more memory
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = { c: i for i, c in enumerate(order)}
        def f(w):
            return [d[c] for c in w]
        words = [ f(w) for w in words ]
        for w, ww in zip(words, words[1:]):
            if not w <= ww:
                return False
        return True 
