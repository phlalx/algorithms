#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Medium (25.37%)
# Likes:    2642
# Dislikes: 1043
# Total Accepted:    381.5K
# Total Submissions: 1.4M
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# the length of shortest transformation sequence from beginWord to endWord,
# such that:
# 
# 
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
# 
# 
# Note:
# 
# 
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# 
# 
# Example 1:
# 
# 
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# Output: 5
# 
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" ->
# "dog" -> "cog",
# return its length 5.
# 
# 
# Example 2:
# 
# 
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# Output: 0
# 
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
# 
# 
# 
# 
# 
#

# @lc code=start
# TAGS BFS
# TODO two end BFS?

import collections, string

def neighbors(wordlist, v):
    res = []
    for i in range(len(v)):
        lv = list(v)
        for l in string.ascii_lowercase:
            lv[i] = l
            if "".join(lv) in wordlist:
                res.append("".join(lv))
    return res


def bfs(wordlist, w1, w2):
    start = collections.deque([w1])
    dist = { w1: 1 }
    while start:
        vertice = start.popleft()
        if vertice == w2:
            return dist[vertice]
        for n in neighbors(wordlist, vertice):
            if not n in dist:
                dist[n] = dist[vertice] + 1
                start.append(n)
    return 0


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        res = bfs(set(wordList), beginWord, endWord)
        return res

# @lc code=end

