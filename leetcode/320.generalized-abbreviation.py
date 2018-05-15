# TAGS recursive, dfs, backtracking
#
# Cool backtracking problem
#
# read carefully the problem, two digits can't follow each other
# Generate all paths of a tree
# Don't compute recursively the set of paths, but stack
# each path and save it at the leaf
#
# @lc app=leetcode id=320 lang=python3
#
# [320] Generalized Abbreviation
#
# https://leetcode.com/problems/generalized-abbreviation/description/
#
# algorithms
# Medium (49.43%)
# Likes:    310
# Dislikes: 32
# Total Accepted:    39.8K
# Total Submissions: 80.5K
# Testcase Example:  '"word"'
#
# Write a function to generate the generalized abbreviations of a word.
#
# Note: The order of the output does not matter.
#
# Example:
#
# Input: "word"
# Output:
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1",
# "w1r1", "1o2", "2r1", "3d", "w3", "4"]
#

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        cur = []
        res = []
        n = len(word)
        def f(i):
            if i == n:
                res.append(''.join(cur))
                return
            cur.append(word[i])
            f(i+1)
            cur.pop()
            for k in range(1, n + 1 - i):
                if cur and cur[-1].isdigit():
                    continue
                cur.append(str(k))
                f(i + k)
                cur.pop()
        f(0)
        return res

