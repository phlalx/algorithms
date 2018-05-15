#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (60.56%)
# Likes:    2103
# Dislikes: 66
# Total Accepted:    123K
# Total Submissions: 198.6K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
#
# Given a list of daily temperatures T, return a list such that, for each day
# in the input, tells you how many days you would have to wait until a warmer
# temperature.  If there is no future day for which this is possible, put 0
# instead.
#
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76,
# 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
#
#
# Note:
# The length of temperatures will be in the range [1, 30000].
# Each temperature will be an integer in the range [30, 100].
#
#
#  Trivial solution: O(n^2)
#  for each i, lookup first element greater than i
#
#  But we can store seen element in a monotonic stack to avoid scanning
#  all elements after j each time.
#
#  This comes from the following observation
#
#  Suppose last three elements are 90 80 100
#  There is no scenario in which next warmer temperature will be 80
#  So we only need to keep (indices of) 90 and 100

# @lc code=start
class Solution:
    def dailyTemperatures(self, T):
        n = len(T)
        st = []
        res = [ None ] * n
        for i in reversed(range(n)):
            x = T[i]
            while st and T[st[-1]] <= x:
                st.pop()
            res[i] = st[-1] - i  if st else 0
            st.append(i)
        return res

# @lc code=end

