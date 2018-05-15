from collections import Counter

class Solution:
    def isAnagram(self, s, t):
        c1 = Counter(s)
        c2 = Counter(t)
        for k in c1:
            if c1[k] != c2[k]:
                return False
        if len(c1) != len(c2):
            return False
        return True
