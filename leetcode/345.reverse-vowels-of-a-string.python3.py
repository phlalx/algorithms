# TAGS string
vowels = "aeiouAEIOU"


def reverse_vowels(s):
    l = list(s)
    i = 0
    j = len(s) - 1
    isVowel = lambda i: l[i] in vowels
    while i < j:
        if isVowel(i) and isVowel(j):
            l[i], l[j] = l[j], l[i]
            i = i + 1
            j = j - 1
        elif isVowel(i):
            j = j - 1
        elif isVowel(j):
            i = i + 1
        else:
            i = i + 1
            j = j - 1
    return "".join(l)


class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        return reverse_vowels(s)
