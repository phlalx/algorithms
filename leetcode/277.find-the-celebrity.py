# TAGS ad-hoc, hard, trick

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

# Condition necessaire / suffisante

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        for i in range(1, n):
            if knows(i, candidate):
                # i can't be candidate because he knows someone
                pass
            else:
                # i doesn't know candidate
                # candidate is not the celebrity
                # and all i smaller than candidate were disqualified
                # so i becomes new candidate
                candidate = i
        # we need to check that candidate doesn't know anybody
        # and that everybody smaller than candidate knows it
        for i in range(n):
            if i != candidate and knows(candidate, i):
                return -1
        for i in range(candidate):
            if not knows(i, candidate):
                return -1
        return candidate
