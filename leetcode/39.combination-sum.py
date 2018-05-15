#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (50.53%)
# Likes:    3146
# Dislikes: 100
# Total Accepted:    481.3K
# Total Submissions: 895.1K
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where the
# candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of
# times.
#
# Note:
#
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
#
#
#
# First idea is DP, but quite tedious to return the solution.
#
#



# Super mega classic
# TAGS dfs, backtrack

# @lc code=start
class Solution:

    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:


        # we print all paths in the DAG of nodes <target, i>
        # where target is the number that we try to find a sum of
        # i is the first index we consider
        # we need to use i to make sure we retruns elements in the right order
        # this avoid duplicate modulo sorting
        #
        # This is simple but we potentially redo the same computation
        # multiple times. We treat the DAG as if it were a tree in the sense
        # that we don't store intermediary results.
        #
        # This is a bit tricky to understand.
        #
        # consider target = 13  and nums = [13, 2, 4]
        #
        #              13
        #        0      11   9
        #                  7
        #
        #    We're going to walk the tree rooted in 7 twice just to realize
        #    it doesn't reach a solution
        #
        #   The best way to do it would be to trim the DAG first,
        #   and only then enumerate the paths via DFS

        # n = len(candidates)
        # path = []
        # sols = []
        # def dfs(target, i):
        #     if target == 0 and i == n:
        #         sols.append(path.copy())
        #     elif i < n:
        #         dfs(target, i+1)  # don't use current numbers
        #         c = candidates[i]
        #         if target - c >= 0:
        #             path.append(c)
        #             dfs(target - c, i)
        #             path.pop()
        # dfs(target, 0)
        # return sols

    # This should be a better solution, but it's not faster
    # maybe the tests cases don't exhibit the bad behavior 

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)

        memo = {}

        def f(i, target):
            res = memo.get((i, target))
            if res is not None:
                return res
            if i == n:
                res = target == 0
            else:
                res = f(i+1, target)
                if target - candidates[i] >= 0:
                    res = res or f(i, target - candidates[i])
            memo[(i, target)] = res
            return res

        f(0, target)

        sols = []
        path = []
        def g(i, target):
            if i == n and target  == 0:
                sols.append(path.copy())
            else:
                if f(i+1, target):
                    g(i+1, target)
                if target - candidates[i] >= 0 and f(i, target - candidates[i]):
                    path.append(candidates[i])
                    g(i, target - candidates[i])
                    path.pop()
        g(0, target)

        return sols

# @lc code=end

