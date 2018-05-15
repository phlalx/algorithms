#
# @lc app=leetcode id=877 lang=python3
#
# [877] Stone Game
#
# https://leetcode.com/problems/stone-game/description/
#
# algorithms
# Medium (64.08%)
# Likes:    610
# Dislikes: 932
# Total Accepted:    52.7K
# Total Submissions: 82.2K
# Testcase Example:  '[5,3,4,5]'
#
# Alex and Lee play a game with piles of stones.  There are an even number of
# piles arranged in a row, and each pile has a positive integer number of
# stones piles[i].
#
# The objective of the game is to end with the most stones.  The total number
# of stones is odd, so there are no ties.
#
# Alex and Lee take turns, with Alex starting first.  Each turn, a player takes
# the entire pile of stones from either the beginning or the end of the row.
# This continues until there are no more piles left, at which point the person
# with the most stones wins.
#
# Assuming Alex and Lee play optimally, return True if and only if Alex wins
# the game.
#
#
#
# Example 1:
#
#
# Input: [5,3,4,5]
# Output: true
# Explanation:
# Alex starts first, and can only take the first 5 or the last 5.
# Say he takes the first 5, so that the row becomes [3, 4, 5].
# If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10
# points.
# If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win
# with 9 points.
# This demonstrated that taking the first 5 was a winning move for Alex, so we
# return true.
#
#
#
#
# Note:
#
#
# 2 <= piles.length <= 500
# piles.length is even.
# 1 <= piles[i] <= 500
# sum(piles) is odd.
#
#

# There are several ways to state the dp relation
#
# A = False
# B = True
#
# A is the first player
#
# For all of them, we define the score of a player as
# score(player) =  points(player) - points(not player)
#
# We define the score of the game as
# score = point(A) - point(B)
#
# Each player tries to maximize its score
#
# Idea 1
# f(i, j, player) -> int
#
# What is the best score achievable by `player`? we suppose player False
# tries to minimize its score, and player True tries to maximize its score
# (minimax)
#

# Idea 2
#
# f(i, j) -> int
#
# We don't really need to distinguish between the players
# because the game is symetric, we suppose the other play just tries to
# maximize `-f`
#
# TODO try to grok that
#



# @lc code=start
import functools

class Solution1:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        @functools.lru_cache(maxsize=None)
        def f(i, j, player) -> int:
            if i == j:
                return piles[i] * (1 if player else -1)
            else:
                if player:
                    return max(f(i+1, j, not player) + piles[i], f(i, j-1, not player) + piles[j] )
                else:
                    return min(f(i+1, j, not player) - piles[i], f(i, j-1, not player) - piles[j] )
        return f(0, n-1, False) < 0

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        @functools.lru_cache(maxsize=None)
        def f(i, j) -> int:
            if i == j:
                return piles[i]
            else:
                return max(piles[i] - f(i+1, j), piles[j] - f(i, j-1))
        return f(0, n-1) > 0


# @lc code=end

