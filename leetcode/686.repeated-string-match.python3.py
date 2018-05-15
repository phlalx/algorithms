# TAGS string, cool
#
# A bit tricky to get right, easy once we read the solution
# reason by necessary condition
# . find biggest possible n
# . find the right n
#


def how_many_repeat(a, b):
    # In the worst case, the repeated string must be long enough to contain
    # max_len_repeated_string. This is the case where B starts on the
    # last element of A
    max_len_repeated_string = len(a) + len(b) - 1
    # at most, n = max_rep
    max_rep = (max_len_repeated_string + len(a) - 1) // len(a)
    rep_str = a * max_rep
    index = rep_str.find(b)
    if index == -1:
        return -1
    actual_size = index + len(b)
    return (actual_size + len(a) - 1) // len(a)


class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        return how_many_repeat(A, B)
