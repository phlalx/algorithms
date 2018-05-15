# TODO
# s is a valid palindrome but we can ignore up to n letters
def validPalindromeIter(s, i, j):
    assert i <= j
    while i < j:
        if s[i] != s[j]:
            return False, i, j
        i = i + 1
        j = j - 1
    return True, None, None


def validPalindromeRec(s, i, j):
    if i >= j:
        return True
    elif s[i] == s[j]:
        return validPalindromeRec(s, i + 1, j - 1)
    else:
        return validPalindromeRec(s, i + 1, j) or validPalindromeRec(s, i, j - 1)


def validPalindromeSkipOne(s):
    isPal, i, j = validPalindromeIter(s, 0, len(s) - 1)
    if isPal:
        return True
    else:
        assert i != j
        return (
            validPalindromeIter(s, i + 1, j)[0] or validPalindromeIter(s, i, j - 1)[0]
        )


class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return validPalindromeSkipOne(s)
