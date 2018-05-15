#
# @lc app=leetcode id=857 lang=python3
#
# [857] Minimum Cost to Hire K Workers
#
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/description/
#
# algorithms
# Hard (48.22%)
# Likes:    793
# Dislikes: 76
# Total Accepted:    26.8K
# Total Submissions: 54.2K
# Testcase Example:  '[10,20,5]\n[70,50,30]\n2'
#
# There are N workers.  The i-th worker has a quality[i] and a minimum wage
# expectation wage[i].
#
# Now we want to hire exactly K workers to form a paid group.  When hiring a
# group of K workers, we must pay them according to the following rules:
#
#
# Every worker in the paid group should be paid in the ratio of their quality
# compared to other workers in the paid group.
# Every worker in the paid group must be paid at least their minimum wage
# expectation.
#
#
# Return the least amount of money needed to form a paid group satisfying the
# above conditions.
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: quality = [10,20,5], wage = [70,50,30], K = 2
# Output: 105.00000
# Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
#
#
#
# Example 2:
#
#
# Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
# Output: 30.66667
# Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers
# seperately.
#
#
#
#
# Note:
#
#
# 1 <= K <= N <= 10000, where N = quality.length = wage.length
# 1 <= quality[i] <= 10000
# 1 <= wage[i] <= 10000
# Answers within 10^-5 of the correct answer will be considered correct.
#
# TAGS greedy, problem solving, optimization
#
# The trick is to see that there will be a worker paid exactly its minimal
# wage in the group then try all such workers (*analyse-synthèse*).
# Very cool original problem.
#
# Suppose this worker is given and call it p.
#
# The wage in his group is W_K = M_p / Q_p * (sum(Q_i for i in K))
#
# The group is fully determined by the worker. We want the minimal quality
# but all workers should be such that M_p / Q_p * Q_i >= M_i,
#   (equivalent to M_p / Q_p >= M_i / Q_i)
#
# p is the worse worker in the group, because for a given quality it is
# more expensive. Let's call him the leader.
#
# TODO can rewrite cleaner code https://leetcode.com/problems/minimum-cost-to-hire-k-workers/discuss/141768/Detailed-explanation-O(NlogN)

# @lc code=start
from heapq import heapify, heappop, heappush

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        n = len(quality)
        # inverse of efficiency, the lowest the better
        key = lambda x: x[0] / x[1]
        qw = sorted(list(zip(wage, quality)), key=key)
        leader = K - 1  # last element of group, the worse ones

        # qualities of everybody besides the leader
        heap = [ -q for _, q in qw[:leader] ]
        heapify(heap)
        # total_wage to pay, leader is index of leader, total_ q is total
        # quality of everybody besides the leader
        f = lambda leader, heap : key(qw[leader]) * (-sum(heap) + qw[leader][1])
        best = f(leader, heap)
        # this is the first candidate result. We can consider other leaders.
        for i in range(K, n):
            old_leader_quality = qw[i-1][1]
            heappush(heap, -old_leader_quality)
            heappop(heap)  # remove worst one
            best = min(best, f(i, heap))
        return best

# @lc code=end

