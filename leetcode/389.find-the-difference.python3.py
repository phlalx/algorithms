# def find_letter(s, t):
#   c = { l : 0 for l in string.ascii_lowercase }
#   for l in t:
#     c[l] = c[l] + 1
#   for l in s:
#     c[l] = c[l] - 1
#   res = ( letter for letter, count in c.items() if count == 1 )
#   return next(res)

from collections import Counter


def find_letter(s, t):
    cs = Counter(s)
    ct = Counter(t)
    for k in ct:
        if cs[k] != ct[k]:
            return k


class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return find_letter(s, t)
