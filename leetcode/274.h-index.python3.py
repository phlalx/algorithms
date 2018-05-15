# TAGS array
# can we do without a sort?


def hindex(citations):
    citations.sort(reverse=True)
    i = 0
    n = len(citations)
    while i < n and citations[i] >= i + 1:
        i = i + 1
    return i


class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        return hindex(citations)
