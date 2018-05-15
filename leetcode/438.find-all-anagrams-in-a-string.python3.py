from collections import Counter


def is_null(count):
    return not any(count.values())


def f(s, p):
    count = Counter(p)
    n = len(s)
    k = len(p)
    if n < k:
        return []
    res = []
    for c in s[:k]:
        count[c] -= 1
    if is_null(count):
        res.append(0)
    for i in range(1, n - k + 1):
        count[s[i - 1]] += 1
        count[s[i + k - 1]] -= 1
        if is_null(count):
            res.append(i)

    return res


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        return f(s, p)
