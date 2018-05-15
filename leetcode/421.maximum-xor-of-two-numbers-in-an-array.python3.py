# TAGS trie, bits, trick
#
# Trick here is to use a trie
# We insert each letter in the trie based on its binary representation
# Given a non empty trie, we can compute in one pass (basically one custom
# find) the max xor between this number and all numbers in the tree. 


def insert(s, trie):
    # very simple to insert, because all words have the same length
    # no need to mark the node of trie
    for d in s:
        trie = trie.setdefault(d, {})


def find(trie, s):
    # return the max xor between s and all element of trie!
    # variant of regular find
    res = 0
    for d in s:
        res = 2 * res
        not_d = "0" if d == "1" else "1"
        t = trie.get(not_d)
        # TRICK: either d or not_d is in the tree
        #    because all numbers have 32 bits, all leaves in the tree
        #    have height 32
        # we try first not_d to maximize the result
        if t is None:
            t = trie[d]
        else:
            res += 1
        trie = t
    return res


class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        trie = {}
        for i in nums:
            s = bin(i)[2:].zfill(32)  # pythonic
            insert(s, trie)
            res = max(res, find(trie, s))
        return res
