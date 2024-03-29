#TAGS intervals

# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#
# https://leetcode.com/problems/meeting-rooms-ii/description/
#
# algorithms
# Medium (43.51%)
# Likes:    1636
# Dislikes: 27
# Total Accepted:    182.1K
# Total Submissions: 418.2K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
# required.
# 
# Example 1:
# 
# 
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# 
# Example 2:
# 
# 
# Input: [[7,10],[2,4]]
# Output: 1
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        l = []
        for a, b in intervals:
            l.append([a, 1])
            l.append([b, -1])
        l.sort()
        res = 0
        cur = 0
        for _t, w in l:
            cur += w
            res = max(res, cur)
        return res

