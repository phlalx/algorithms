#TAGS dag, graph, dp, greedy, cool
#
# Trick: looks like LIS, but is different because we can reorder the
#        elements. Could be a general longest path in a DAG but overkill.
#        There's a simple greedy solution.
#
#        Think what is the first element of the solution. It is necessarily
#        the one with the smallest right. Then the second element is the
#        one with the smallest right after the first one...
#
#        So we can simply order all the element on the right value. And
#        choose greedily the next element.
#

class Solution:
    def findLongestChain(self, pairs):
        if not pairs:
            return 0
        pairs.sort(key = lambda x: x[1])
        cur_right = pairs[0][1]
        res = 1
        for left, right in pairs[1:]:
            if left > cur_right:
                res += 1
                cur_right = right
        return res

# from collections import defaultdict
# Solution 1: longest path in DAG
#
# longest path in a DAG
# class Solution:
#     def findLongestChain(self, pairs):
#         pairs = [tuple(p) for p in pairs]
#         pairs.sort()
#         neigh = defaultdict(list)
#         seen = {}
#         n = len(pairs)
#         for i, p in enumerate(pairs):
#             seen[p] = None
#             j = n - 1
#             while j >= i + 1 and pairs[j][0] > pairs[i][1]:
#                 neigh[p].append(pairs[j])
#                 j -= 1
#         def dfs(i):
#             if seen[i] is not None:
#                 return seen[i]
#             res = 0
#             for j in neigh[i]:
#                 res = max(res, 1 + dfs(j))
#             seen[i] = res
#             return res
#         return max(dfs(p) for p in seen.keys()) + 1

# Solution 2:
#
# class Solution:
#     def findLongestChain(self, pairs):
#         pairs.sort()
#         n = len(pairs)
#         memo = [[ None ] * (n + 1) for _ in range(n+1)]
#         n = len(pairs)
#         def dp(i, last):
#             if last is None:
#                 last_i = 0
#             else:
#                 last_i = last + 1
#             if memo[i][last_i] is not None:
#                 return memo[i][last_i]
#             if i == n:
#                 return 0
#             res = dp(i+1, last)
#             if last is None or pairs[last][1] < pairs[i][0]:
#                 res = max(res, 1 + dp(i+1, i))
#             memo[i][last_i] = res
#             return res

#         return dp(0, None)
