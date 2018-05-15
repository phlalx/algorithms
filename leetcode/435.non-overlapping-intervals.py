#TAGS greedy, intervals, cool
#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#
# https://leetcode.com/problems/non-overlapping-intervals/description/
#
# algorithms
# Medium (41.85%)
# Likes:    570
# Dislikes: 25
# Total Accepted:    45.7K
# Total Submissions: 109.3K
# Testcase Example:  '[[1,2]]'
#
# Given a collection of intervals, find the minimum number of intervals you
# need to remove to make the rest of the intervals non-overlapping.
#
#
#
#
#
#
# Example 1:
#
#
# Input: [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of intervals are
# non-overlapping.
#
#
# Example 2:
#
#
# Input: [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of intervals
# non-overlapping.
#
#
# Example 3:
#
#
# Input: [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're
# already non-overlapping.
#
#
#
#
# Note:
#
#
# You may assume the interval's end point is always bigger than its start
# point.
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap
# each other.
#
#
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        cur_end = intervals[0][1]
        res = 0
        for inter_start, inter_end in intervals[1:]:
            if cur_end > inter_start:
                res += 1
                cur_end = min(cur_end, inter_end)
            else:
                cur_end = inter_end
        return res

# @lc code=end

