# TAGS double pointer

# This is a *double pointer* problem which can be generalized.
# We look for the smallest window s[i:j+1] of s that satisfies a predicate P(i, j).
#
# For each i, we look for the first j (if it exists) such that the predicate
# holds. We keep the smallest windows among these. O(n^2)
#
# However, if P satisfies some "monoticity" properties, we can test only
# O(n) windows as we never need to decrement j.

from collections import Counter


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        n = len(s)
        count = Counter(t)
        missing = len(count)
        i = 0
        I, J = None, None
        for j in range(n):
            if s[j] not in count:
                continue
            count[s[j]] -= 1
            if count[s[j]] == 0:
                missing -= 1
            if missing > 0:
                continue
            while i <= j and missing == 0:
                if I is None or j - i < J - I:
                    I, J = i, j
                if s[i] not in count:
                    i += 1
                    continue
                count[s[i]] += 1
                if count[s[i]] == 1:
                    missing += 1
                i += 1
        return s[I : J + 1] if I is not None else ""


# My initial solution, dp with bitset. TLE and way too complicated

# def add(bits, i):
#     return bits | 1 << i

# # NOTE on negative num in python  ~x is defined as  -x - 1
# def rem(bits, i):
#     return bits & ~(1 << i)

# class Solution:
#     def minWindow(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         d = { l : [] for l in t }
#         for i, l in enumerate(t):
#             d[l].append(i)

#         ALL = 1 << len(t)

#         memo = [ [float('inf')] * ALL for _ in range(2) ]
#         memo[0][0] = 0

#         m = 0
#         cur_min = float('inf')
#         cur_i = None

#         for i in reversed(range(len(s))):
#             indices = d.get(s[i])
#             next_m = (m+1) % 2
#             for bits in range(ALL):
#                 res = memo[m][bits]
#                 if indices:
#                     for j in indices:
#                         res = min(res, memo[m][rem(bits, j)])
#                 memo[next_m][bits] = res + 1
#                 memo[next_m][0] = 0

#             if memo[next_m][ALL-1] < cur_min:
#                 cur_min = memo[next_m][ALL-1]
#                 cur_i = i

#             m = (m+1) % 2

#         if cur_min != float('inf'):
#             return s[cur_i:cur_i+cur_min]
#         else:
#             return ""
