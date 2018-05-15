#TAGS hard, backtrack
# Took this solution from https://leetcode.com/problems/optimal-account-balancing/discuss/95355/Concise-9ms-DFS-solution-(detailed-explanation)
# but not really getting it

from collections import Counter

class Solution:
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        m = Counter()

        for u, v, w in transactions:
            m[u] -= w
            m[v] += w

        debt = [u for u in m.values() if u]
        n = len(debt)

        def dfs(s):
            while s < n and debt[s] == 0:
                s += 1
            if s == n:
                return 0

            r = float('inf')
            for i in range(s+1, n):
                if debt[i] * debt[s] < 0:
                    # settle s with i
                    debt[i] += debt[s]
                    r = min(r, 1 + dfs(s+1))
                    # backtrack
                    debt[i] -= debt[s]
            return r

        return dfs(0)
