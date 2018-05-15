#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (29.88%)
# Likes:    1350
# Dislikes: 76
# Total Accepted:    129.2K
# Total Submissions: 432.3K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
  '["oath","pea","eat","rain"]'
#
# Given a 2D board and a list of words from the dictionary, find all words in
# the board.
#
# Each word must be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring. The
# same letter cell may not be used more than once in a word.
#
#
#
# Example:
#
#
# Input:
# board = [
# ⁠ ['o','a','a','n'],
# ⁠ ['e','t','a','e'],
# ⁠ ['i','h','k','r'],
# ⁠ ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]
#
# Output: ["eat","oath"]
#
#
#
#
# Note:
#
#
# All inputs are consist of lowercase letters a-z.
# The values of words are distinct.
#
#
#
#TAGS trie, backtrack
#
# Not hard, got it almost on the first try

# @lc code=start

def insert(trie, word):
    for c in word:
        trie = trie.setdefault(c, {})
    trie[None] = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        if not board or not board[0]:
            return []

        n = len(board)
        p = len(board[0])

        res = set()
        path = []

        def neighbors(i, j):
            for di, dj in zip([0, 1, 0, -1], [1, 0, -1, 0]) :
                ii = i + di
                jj = j + dj
                if 0 <= ii < n and 0 <= jj < p and (ii, jj) not in path:
                    yield ii, jj

        def search(i, j, trie):
            c = board[i][j]
            if c not in trie:
                return
            trie = trie[c]
            if None in trie:
                res.add(trie[None])

            path.append((i, j))
            for ii, jj in neighbors(i, j):
                search(ii, jj, trie)
            path.pop()

        trie = {}
        for word in words:
            insert(trie, word)
        for i in range(n):
            for j in range(p):
                search(i, j, trie)

        return list(res)



# @lc code=end

