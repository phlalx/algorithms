# TAGS palindrome

import string


def isalphanum(s):
    return s in string.ascii_letters or s in string.digits


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while i < j:
            if not isalphanum(s[i]):
                i = i + 1
                continue
            if not isalphanum(s[j]):
                j = j - 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i = i + 1
            j = j - 1
        return True
