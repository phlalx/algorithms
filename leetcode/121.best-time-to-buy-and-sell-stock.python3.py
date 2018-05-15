# TAGS dp, kadane
# Very simple db
# compute recursively f(i) the best possible deal at time i, and the cur min


class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        best_deal = 0
        cur_min = float("inf")
        for v in prices:
            best_deal = max(best_deal, v - cur_min)
            cur_min = min(cur_min, v)
        return best_deal
