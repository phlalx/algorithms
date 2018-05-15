# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

# TAGS heuristic, interactive
#
# First see there's no way for this to work always in less than 10 attempts.
# Consider aaaaa bbbbb cccccc ddddddd eeeee... no words give us any information
#
#
# Structure is simple: guess a word, and reduce candidate list based on some
# heuristics
#
# At least, we can remove the guess word so this always converges.
# 
# TRICK If w has k matches, then any possible solution has EXACTLY k matches with w. 
#
# Then one can furthermore improve the heuristic. Among all candidates, choose one that
# has a big "family" (big number of words that share letters with it).
#
# See this nice analysis of the problem
# https://leetcode.com/problems/guess-the-word/discuss/133862/Random-Guess-and-Minimax-Guess-with-Comparison
#

import random

def match(word1, word2):
    return sum(a == b for a, b in zip(word1, word2))

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        candidates = wordlist

        for _ in range(10):
            # TODO we could do better here
            # consider a guess where [w | match(guess, w) == 0] is small
            # or a guess such that [w | match(guess, w) = i] is well balanced
            # see different heuristics
            guess = random.choice(candidates)
            match_num = master.guess(guess)
            print(guess, match_num)
            if match_num == 6:
                break
            candidates = [w for w in candidates if match(w, guess) == match_num]

        
