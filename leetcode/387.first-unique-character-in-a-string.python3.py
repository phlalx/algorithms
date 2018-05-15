#TAGS easy
from collections import Counter

class Solution:
    def firstUniqChar(self, s):
        c = Counter(s)
        return next((x for x, v in c.items() if v == 1), -1)