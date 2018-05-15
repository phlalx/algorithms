#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#
# https://leetcode.com/problems/maximum-product-of-word-lengths/description/
#
# algorithms
# Medium (50.75%)
# Likes:    768
# Dislikes: 69
# Total Accepted:    96.3K
# Total Submissions: 189.1K
# Testcase Example:  '["abcw","baz","foo","bar","xtfn","abcdef"]'
#
# Given a string array words, find the maximum value of length(word[i]) *
# length(word[j]) where the two words do not share common letters. You may
# assume that each word will contain only lower case letters. If no such two
# words exist, return 0.
#
# Example 1:
#
#
# Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".
#
# Example 2:
#
#
# Input: ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4
# Explanation: The two words can be "ab", "cd".
#
# Example 3:
#
#
# Input: ["a","aa","aaa","aaaa"]
# Output: 0
# Explanation: No such pair of words.
#
#
#

# @lc code=start
#TAGS bitset, cool, pythonic, trick
# For each set of letters (bitset), record the length of the longest word with
# these letters.
# Then go through all disjoint pairs of sets, and compute the max product
#
# Trick1: for an English langage word, one can represent the set of its letters
# with a 32 bit integer.
#
# Trick2: instead of storing the mask for each word, we just record the length
#         of the max word that has these letters

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = {}
        for w in words:
            mask = 0
            for c in w:
                mask |= 1 << (ord(c) - ord('a'))
            d[mask] = max(d.get(mask, 0), len(w))
        return max((d[m] * d[mm] for m in d for mm in d if m & mm == 0), default=0)

# @lc code=end

