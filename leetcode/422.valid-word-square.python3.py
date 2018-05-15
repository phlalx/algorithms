# TAGS matrix
# A little tricky to get it right...
class Solution:
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        n = len(words)
        i = 0
        while i < n and len(words[i]) >= i + 1:  # words[i][i] is defined
            k = len(words[i])
            if k > n:
                return False
            for u in range(i + 1, k):
                if len(words[u]) <= i or words[i][u] != words[u][i]:
                    return False
            # make sure words[k][u] isn't defined
            if k < n and len(words[k]) > i:
                return False
            i += 1
        if i < n and any(len(words[u]) > i for u in range(i + 1, n)):
            return False

        return True
