#TAGS 2-sum, de-duplicate

from collections import Counter

def next_unique(s):
    last = None
    for c in s:
        if c == last:
            continue
        last = c
        yield c

def deduplicate(s):
    i = 0
    for c in next_unique(s):
        s[i] = c
        i += 1
    return s[:i]

class Solution:
    def findPairs(self, nums, k):
        # beware of edge case
        if k == 0:
            l = Counter(nums)
            return sum(1 for k, v in l.items() if v >= 2)
        # l = sorted(list(set(nums))) # overkill
        nums.sort()
        l = deduplicate(nums)
        seen = set()
        res = 0
        for c in l:
            if c - k in seen:
                res += 1
            seen.add(c)
        return res
