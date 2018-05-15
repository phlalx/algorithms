#TAGS brute force, dfs, dp, trie
# Similar to 39 (combination sum), example of a DP problem
# where we print all the solutions
#  memo represents a DAG that we walk like a tree
#  using backtracking
#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (28.14%)
# Likes:    1142
# Dislikes: 264
# Total Accepted:    172.9K
# Total Submissions: 614.4K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, add spaces in s to construct a sentence where each word is a
# valid dictionary word. Return all such possible sentences.
#
# Note:
#
#
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
#
#
# Example 1:
#
#
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
# "cats and dog",
# "cat sand dog"
# ]
#
#
# Example 2:
#
#
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
#
#

# Simple solution, but TLE

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        memo = [ None ] * (n + 1)
        memo[n] = [[]]
        #  there is one empty sentence (different than no
        # sentence at all)

        for i in reversed(range(n)):
            sentences = []
            for w in wordDict:
                if s.startswith(w, i):
                    for sentence in memo[i + len(w)]:
                        sentences.append([w] + sentence)
            memo[i] = sentences
        return [ ' '.join(w) for w in memo[0] ]

# store all paths
def f(i, memo, sentence, res, n):
    if i == n:
        res.append(' '.join(sentence))
        return
    for (w, k) in memo[i]:
        sentence.append(w)
        f(k, memo, sentence, res, n)
        sentence.pop()
    return

def addword(trie, word):
    for c in word:
        trie = trie.setdefault(c, {})
    trie['word'] = word   # don't bother with a class Trie to store this addditional
                         # field

# iterator over words in trie starting from i in s
def words(trie, s, i):
    n = len(s)
    while i < n:
        c = s[i]
        trie = trie.get(c, None)
        if trie is None:
            break
        word = trie.get('word', None)
        if word is not None:
            yield word
        i += 1

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        trie = {}
        n = len(s)
        for word in wordDict:
            addword(trie, word)

        memo = {}
        memo[n] = [[]]
        def can_decode(i):
            res = memo.get(i)
            if res is not None:
                return res
            res = []
            for w in words(trie, s, i):
                if can_decode(i + len(w)):
                    res.append((w, i + len(w)))
            memo[i] = res
            return res
        can_decode(0)

        res = []
        sentence = []
        f(0, memo, sentence, res, n)
        return res
