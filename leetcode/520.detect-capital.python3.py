# TAGS string


class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) <= 1:
            return True
        it = iter(word)
        a = next(it)
        b = next(it)
        if b.isupper():
            return a.isupper() and all(x.isupper() for x in it)
        else:
            return all(x.islower() for x in it)

    # Solution 2: seems to be the best solution but slower than solution 1?
    #     if len(word) <= 1:
    #         return True
    #     if word[1].isupper():
    #         return word.isupper()
    #     else:
    #         return word[1:].islower() # careful here, ''.islower() return False

    # Solution 3, a 4 states automata
    # def detectCapitalUse(self, word):
    #     """
    #     :type word: str
    #     :rtype: bool
    #     """
    #     state = 0
    #     for c in word:
    #         isup = c.isupper()
    #         if state == 0:
    #             state = 1 if isup else 2
    #         elif state == 1:
    #             state = 3 if isup else 2
    #         elif state == 2:
    #             if isup:
    #                 return False
    #         else:
    #             if not isup:
    #                 return False
    #     return True
