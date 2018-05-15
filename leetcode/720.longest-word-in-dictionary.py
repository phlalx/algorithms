#
# @lc app=leetcode id=720 lang=python3
#
# [720] Longest Word in Dictionary
#
# https://leetcode.com/problems/longest-word-in-dictionary/description/
#
# algorithms
# Easy (45.70%)
# Likes:    520
# Dislikes: 649
# Total Accepted:    54.6K
# Total Submissions: 115.1K
# Testcase Example:  '["w","wo","wor","worl","world"]'
#
# Given a list of strings words representing an English Dictionary, find the
# longest word in words that can be built one character at a time by other
# words in words.  If there is more than one possible answer, return the
# longest word with the smallest lexicographical order.  If there is no answer,
# return the empty string.
# 
# Example 1:
# 
# Input: 
# words = ["w","wo","wor","worl", "world"]
# Output: "world"
# Explanation: 
# The word "world" can be built one character at a time by "w", "wo", "wor",
# and "worl".
# 
# 
# 
# Example 2:
# 
# Input: 
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# Output: "apple"
# Explanation: 
# Both "apply" and "apple" can be built from other words in the dictionary.
# However, "apple" is lexicographically smaller than "apply".
# 
# 
# 
# Note:
# All the strings in the input will only contain lowercase letters.
# The length of words will be in the range [1, 1000].
# The length of words[i] will be in the range [1, 30].
# 
#

# @lc code=start
# TAGS trie, dfs
# Cool exercise, combine trie construction + walk of a tree
# TODO very slow... maybe there's a more pythonic solution?

# Solution 1, using specialized trie and pre-sort the input


def insert(trie, w, i):
    n = len(w)
    if i == n:
        return True
    t = trie.get(w[i])
    if t is None:
        if i != n - 1:
            return False
        else:
            t = trie.setdefault(w[i], {})
    return insert(t, w, i + 1)


def main(words):
    words.sort(key=lambda w: (len(w), w))
    cur = ""
    trie = {}
    for w in words:
        if insert(trie, w, 0) and len(w) > len(cur):
            cur = w
    return cur


# Solution 2 no pre-sorting and generic trie, better complexity


class Trie(dict):
    # little trick, extends dict and keep a word to avoid reconstructing
    # it later, and to know if a node corresponds to a word
    def __init__(self, word=None):
        self.word = word


def insert(trie, w):
    for c in w:
        trie = trie.setdefault(c, Trie())
    trie.word = w


def walk(trie):
    assert trie.word is not None
    res = trie.word
    for _, trie in trie.items():
        if trie.word is None:
            continue
        cur_res = walk(trie)
        if len(cur_res) > len(res) or len(cur_res) == len(res) and cur_res < res:
            res = cur_res
    return res


def main(words):
    trie = Trie(word="")
    for w in set(words):
        insert(trie, w)
    return walk(trie)


class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        return main(words)

# @lc code=end

