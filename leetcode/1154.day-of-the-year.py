#
# @lc app=leetcode id=1154 lang=python3
#
# [1154] Day of the Year
#
# https://leetcode.com/problems/day-of-the-year/description/
#
# algorithms
# Easy (49.18%)
# Likes:    53
# Dislikes: 98
# Total Accepted:    11.7K
# Total Submissions: 23.9K
# Testcase Example:  '"2019-01-09"\r'
#
# Given a string date representing a Gregorian calendar date formatted as
# YYYY-MM-DD, return the day number of the year.
# 
# 
# Example 1:
# 
# 
# Input: date = "2019-01-09"
# Output: 9
# Explanation: Given date is the 9th day of the year in 2019.
# 
# 
# Example 2:
# 
# 
# Input: date = "2019-02-10"
# Output: 41
# 
# 
# Example 3:
# 
# 
# Input: date = "2003-03-01"
# Output: 60
# 
# 
# Example 4:
# 
# 
# Input: date = "2004-03-01"
# Output: 61
# 
# 
# 
# Constraints:
# 
# 
# date.length == 10
# date[4] == date[7] == '-', and all other date[i]'s are digits
# date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.
# 
#
# TAGS calendar

# @lc code=start
class Solution:
    def dayOfYear(self, date):
        year, month, day = [int(x) for x in date.split('-')]
        feb = 29 if year % 4 == 0 and (year % 100 != 0 or (year / 100 % 4) == 0) else 28
        months = [31,feb,31,30,31,30,31,31,30,31,30,31]
        return sum(months[:month - 1]) + day

# @lc code=end

