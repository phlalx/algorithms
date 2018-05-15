#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (43.31%)
# Likes:    1431
# Dislikes: 56
# Total Accepted:    296.5K
# Total Submissions: 642.8K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sums to target.
# 
# Each number in candidates may only be used once in the combination.
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
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
# [1,2,2],
# [5]
# ]
# 
# 
#
# TAGS backtrack
# almost identical to combination sum i
# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        path = []
        sols = set()
        candidates.sort(reverse=True)  # optimization?
        def dfs(target, i):
            if target == 0 and i == n:
                sols.add(tuple(path))
            elif i < n:
                dfs(target, i+1)  # don't use current numbers
                c = candidates[i]
                if target - c >= 0:
                    path.append(c)
                    dfs(target - c, i+1)
                    path.pop()
        dfs(target, 0)
        return sols
 
# @lc code=end

