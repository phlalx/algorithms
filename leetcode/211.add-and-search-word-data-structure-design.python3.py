# TAGS datatype cool TODO broken
# simple extension of tree
# search complexity = O(T) instead of O(word)
#
# See also 676
#

from collections import defaultdict


class WordDictionary:
    def __init__(self):
        self._isWord = False
        self._children = defaultdict(WordDictionary)

    def addWord(self, w):
        cur = self
        for c in w:
            cur = cur._children[c]
        cur._isWord = True

    def search(self, word):
        cur = self
        for c in word:
            if c in cur._children:
                cur = cur._children[c]
            else:
                return False
        return cur._isWord


def test():
    wd = WordDictionary()
    wd.addWord("one")
    wd.addWord("two")
    wd.addWord("three")
    for w in ["one", "two", "three"]:
        assert wd.search(w)
    for w in ["o", "t", "", "oneo"]:
        assert not wd.search(w)


# test()

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Design a data structure that supports the following two operations:


# void addWord(word)
# bool search(word)


# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.


# For example:

# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true


# Note:
# You may assume that all words are consist of lowercase letters a-z.


# click to show hint.

# You should be familiar with how a Trie works. If not, please work on this problem: Implement Trie (Prefix Tree) first.
