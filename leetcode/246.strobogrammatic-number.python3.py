# TAGS palindrome


def symetric(d1, d2):
    if d1 == "1":
        return d2 == "1"
    elif d1 == "6":
        return d2 == "9"
    elif d1 == "9":
        return d2 == "6"
    elif d1 == "0":
        return d2 == "0"
    elif d1 == "8":
        return d2 == "8"
    return False


class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = (len(num) + 1) // 2
        for i in range(n):
            if not symetric(num[i], num[-i - 1]):
                return False
        return True
