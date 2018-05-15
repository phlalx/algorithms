# TAGS array, pythonic, cool
# TODO can we do better than O(n^2)

import collections
import itertools

# [-1,0,1] and [0,1,-1] are considered to be the same vector

# TLE
class Solution:
    def threeSum(self, nums):
        s = set()
        for l in itertools.combinations(nums, 3):
            if sum(l) == 0:
                x = tuple(sorted(l))
                s.add(x)
        return list(s)


# TLE probably what is expected
def f(nums):
    n = len(nums)
    seen = set()
    res = set()
    for i in range(n):
        a = nums[i]
        for j in range(i + 1, n):
            b = nums[j]
            if -(a + b) in seen:
                res.add(tuple(sorted([-a - b, a, b])))
        seen.add(a)
    return list(list(u) for u in res)


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        counter = collections.Counter(nums)
        res = set()
        for e, ee in itertools.combinations_with_replacement(counter, 2):
            u = -e - ee
            if not u in counter:
                continue
            vec = tuple(sorted([u, e, ee]))
            if vec in res:
                continue
            # concise but slow
            vector_count = collections.Counter(vec)
            if all(vector_count[x] <= counter[x] for x in vec):
                res.add(vec)

        return [list(x) for x in res]
