
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



        
