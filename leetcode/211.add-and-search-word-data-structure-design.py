#
# @lc app=leetcode id=211 lang=python3
#
# [211] Add and Search Word - Data structure design
#
# https://leetcode.com/problems/add-and-search-word-data-structure-design/description/
#
# algorithms
# Medium (31.67%)
# Likes:    1442
# Dislikes: 76
# Total Accepted:    162.1K
# Total Submissions: 465.8K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n' +
  '[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# Design a data structure that supports the following two operations:
# 
# 
# void addWord(word)
# bool search(word)
# 
# 
# search(word) can search a literal word or a regular expression string
# containing only letters a-z or .. A . means it can represent any one letter.
# 
# Example:
# 
# 
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# 
# 
# Note:
# You may assume that all words are consist of lowercase letters a-z.
# 
#

# @lc code=start

from collections import defaultdict


class WordDictionary:
    def __init__(self):
        self._isWord = False
        self._children = {}

    def addWord(self, w):
        cur = self
        for c in w:
            cur = cur._children.setdefault(c, WordDictionary())
        cur._isWord = True

    def search(self, word):
        n = len(word)
        def f(cur, i):
            if i == n:
                return cur._isWord
            elif word[i] in cur._children:
                return f(cur._children[word[i]], i+1)
            elif word[i] == '.':
                return any(f(cur._children[c], i+1) for c in cur._children)
            else:
                return False
        return f(self, 0)

def test():
    wd = WordDictionary()
    wd.addWord("one")
    wd.addWord("two")
    wd.addWord("three")
    for w in ["one", "two", "three"]:
        assert wd.search(w)
    for w in ["o", "t", "", "oneo"]:
        assert not wd.search(w)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

