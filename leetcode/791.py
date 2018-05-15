#TAGS sort
#pythonic: remember how to sort a string (no method sort, an sorted returns
# a list
#TODO
# Follow up 1: If the custom order S is too large, how to solve it efficiently?
# Follow up 2: If the string T is too large, how to solve it efficiently?
# Counting/bucket sort

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        m = { x : i for i, x in enumerate(S) }
        key = lambda x : m.get(x, -1)
        return ''.join(sorted(T, key=key))
        
