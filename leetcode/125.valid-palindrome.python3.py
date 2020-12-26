# TAGS palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i = 0
        j = n-1
        while i < j:
            si = s[i]
            sj = s[j]
            if not si.isalnum():
                i += 1
            elif not sj.isalnum():
                j -= 1
            elif si.lower() == sj.lower():
                i += 1
                j -= 1
            else:
                return False
        return True