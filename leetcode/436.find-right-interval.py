#
# @lc app=leetcode id=436 lang=python3
#
# [436] Find Right Interval
#
# https://leetcode.com/problems/find-right-interval/description/
#
# algorithms
# Medium (43.40%)
# Likes:    256
# Dislikes: 105
# Total Accepted:    29.8K
# Total Submissions: 68.2K
# Testcase Example:  '[[1,2]]'
#
# Given a set of intervals, for each of the interval i, check if there exists
# an interval j whose start point is bigger than or equal to the end point of
# the interval i, which can be called that j is on the "right" of i.
#
# For any interval i, you need to store the minimum interval j's index, which
# means that the interval j has the minimum start point to build the "right"
# relationship for interval i. If the interval j doesn't exist, store -1 for
# the interval i. Finally, you need output the stored value of each interval as
# an array.
#
# Note:
#
#
# You may assume the interval's end point is always bigger than its start
# point.
# You may assume none of these intervals have the same start point.
#
#
#
#
# Example 1:
#
#
# Input: [ [1,2] ]
#
# Output: [-1]
#
# Explanation: There is only one interval in the collection, so it outputs
# -1.
#
#
#
#
# Example 2:
#
#
# Input: [ [3,4], [2,3], [1,2] ]
#
# Output: [-1, 0, 1]
#
# Explanation: There is no satisfied "right" interval for [3,4].
# For [2,3], the interval [3,4] has minimum-"right" start point;
# For [1,2], the interval [2,3] has minimum-"right" start point.
#
#
#
#
# Example 3:
#
#
# Input: [ [1,4], [2,3], [3,4] ]
#
# Output: [-1, 2, -1]
#
# Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
# For [2,3], the interval [3,4] has minimum-"right" start point.
#
#
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
#
#

#TAGS binary search
#TODO there is a better solution

# @lc code=start
def bisect(v, i, j, pred):
    while i < j:
        m = (i + j) // 2
        if pred(v[m]):
            j = m
        else:
            i = m + 1
    if i > j or not pred(v[i]):
        return None
    else:
        return i

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        snd = lambda x: x[1]
        n = len(intervals)
        sorted_intervals = sorted(list(enumerate(intervals)), key=snd)
        res = [ None ] * n
        for i in reversed(range(n)):
            pred = lambda x: x[1][0] >= intervals[i][1]
            x = bisect(sorted_intervals, 0, n-1, pred)
            if x is None:
                res[i] = -1
            else:
                res[i] = sorted_intervals[x][0]
        return res

# @lc code=end

