#
# @lc app=leetcode id=294 lang=python3
#
# [294] Flip Game II
#
# https://leetcode.com/problems/flip-game-ii/description/
#
# algorithms
# Medium (48.82%)
# Likes:    307
# Dislikes: 25
# Total Accepted:    46.3K
# Total Submissions: 94.7K
# Testcase Example:  '"++++"'
#
# You are playing the following Flip Game with your friend: Given a string that
# contains only these two characters: + and -, you and your friend take turns
# to flip two consecutive "++" into "--". The game ends when a person can no
# longer make a move and therefore the other person will be the winner.
#
# Write a function to determine if the starting player can guarantee a win.
#
# Example:
#
#
# Input: s = "++++"
# Output: true
# Explanation: The starting player can guarantee a win by flipping the middle
# "++" to become "+--+".
#
#
# Follow up:
# Derive your algorithm's runtime complexity.
#

# @lc code=start
import functools

class Solution:
    def canWin(self, s: str) -> bool:
        n = len(s)

        @functools.lru_cache(maxsize=None)
        def f(s):
            for i in range(n-1):
                if s[i:i+2] == '++':
                    ss = list(s)
                    ss[i:i+2] = '--'
                    if not f(''.join(ss)):
                        return True
            return False

        return f(s)


# @lc code=end

