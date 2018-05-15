# TAGS string, gcd, trick

import collections


def pgcd(a, b):
    if b == 0:
        return a
    else:
        return pgcd(b, a % b)


def check_repeat(s, p):
    if p == 1:
        return False
    else:
        return s == p * s[: len(s) // p]


def is_repeated(s):
    count = collections.Counter(s)
    p = 0
    for v in count.values():
        p = pgcd(p, v)
    for i in range(2, p + 1):
        if p % i == 0 and check_repeat(s, i):
            return True
    return False


class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return is_repeated(s)


# trick
#
# class Solution:
#     def repeatedSubstringPattern(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         t = s + s
#         return t.find(s, 1) < len(s)
