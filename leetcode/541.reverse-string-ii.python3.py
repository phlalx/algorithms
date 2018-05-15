# TAGS reverse, bounds

# reverse l[i:j] in place
# pythonic but not constant space as we need to allocate new lists
# Nonetheless, faster than the constant space solution `rev_aux`
# remark: l[i:j][::-1] != l[j:i:-1]
def rev_aux_pythonic(l, i, j):
    l[i:j] = l[i:j][::-1]


# reverse l[i:j]  O(1)
def rev_aux(l, i, j):
    first = i
    last = j - 1  # last elt to be swapped
    # less error prone than "for u in range(i, middle)"
    while first < last:
        l[first], l[last] = l[last], l[first]
        first += 1
        last -= 1


def reverse(l, k):
    n = len(l)
    i = 0
    # reverse each sublist of len 2k sequentially
    # last sublist may have small length
    for i in range(0, n, 2 * k):
        last = min(n, i + k)
        rev_aux_pythonic(l, i, last)


class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # string aren't mutable, we convert to/from list
        l = list(s)
        reverse(l, k)
        return "".join(l)
