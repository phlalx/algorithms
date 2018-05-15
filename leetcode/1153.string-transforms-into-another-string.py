#TAGS graph ad-hoc

# Annoying problem
# First part is to find the necessary permutation. Easy.
# Then it seems cycles are problem, but they can be avoided with rewriting
# if one extra char available...
           
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        n = len(str1)
        if len(str2) != n:
            return False
        map = {}
        for a, b in zip(str1, str2):
            if map.setdefault(a, b) != b:
                return False
        return len(set(str2)) < 26
   
        
