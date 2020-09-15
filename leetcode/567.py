#TAGS sliding window
# can be improved by augmenter dict to count zeros

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
      n = len(s2)
      p = len(s1)
      
      if p == 0:
        return True
      if p > n:
        return False
      
      counter = {c:0 for c in string.ascii_lowercase}
      for c in s1:
        counter[c] += 1
      for c in s2[:p]:
        counter[c] -= 1
      
      if not any(counter.values()):
        return True
      
      i = 0
      for j in range(p, n):
        counter[s2[j]] -= 1
        counter[s2[i]] += 1
        i += 1
        if not any(counter.values()):
          return True
      return False
    
