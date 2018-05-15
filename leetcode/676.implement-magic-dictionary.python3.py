# TAGS trie, cool, TODO broken
# See also 211
#
# Careful that we HAVE TO use at least one different letter
#
#
#  Store all words in a trie
#  DFS the trie
#

from collections import defaultdict


class Trie:
    def __init__(self):
        self._isWord = False
        self._children = defaultdict(Trie)

    def insert(self, w):
        cur = self
        for c in w:
            cur = cur._children[c]
        cur._isWord = True

    def search(self, w, i, change):
        if i == len(w):
            return not change
        elif change:
            return any(trie.search(w, i + 1, False) for trie in self._children)
        else:
            if w[i] in self._children:
                return True
            else:
                trie = self._children[w[i]]
                return trie.search(w, i + 1, True)


class MagicDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for w in dict:
            self.trie.insert(w)

    def search(self, w):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        change = True
        return self.trie.search(w, 0, change)


# Alternative solution
#
# Use a dict:
#  Key = (truncated word, missing index)
#  Value = missing letter
#
# Solution 1
#
# class MagicDictionary:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.m = defaultdict(set)

#     def buildDict(self, dict):
#         """
#         Build a dictionary through a list of words
#         :type dict: List[str]
#         :rtype: void
#         """
#         for w in dict:
#             for i in range(len(w)):
#                 c = w[i]
#                 key = w[:i] + w[i+1:], i
#                 s = self.m[key]
#                 s.add(c)

#     def search(self, w):
#         """
#         Returns if there is any word in the trie that equals to the given word after modifying exactly one character
#         :type word: str
#         :rtype: bool
#         """
#         for i in range(len(w)):
#             c = w[i]
#             key = w[:i] + w[i+1:]
#             u = self.m.get((key, i))
#             if u is None:
#                 continue
#             if not {c} == u:
#                 return True

#         return False
