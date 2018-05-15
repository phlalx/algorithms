#
# @lc app=leetcode id=517 lang=python3
#
# [517] Super Washing Machines
#
# https://leetcode.com/problems/super-washing-machines/description/
#
# algorithms
# Hard (37.02%)
# Likes:    236
# Dislikes: 123
# Total Accepted:    14K
# Total Submissions: 37.4K
# Testcase Example:  '[1,0,5]'
#
# You have n super washing machines on a line. Initially, each washing machine
# has some dresses or is empty.
#
#
# For each move, you could choose any m (1 ≤ m ≤ n) washing machines, and pass
# one dress of each washing machine to one of its adjacent washing machines  at
# the same time .
#
# Given an integer array representing the number of dresses in each washing
# machine from left to right on the line, you should find the minimum number of
# moves to make all the washing machines have the same number of dresses. If it
# is not possible to do it, return -1.
#
# Example1
#
# Input: [1,0,5]
#
# Output: 3
#
# Explanation:
# 1st move:    1     0     1     1     4
# 2nd move:    1     2     1     3
# 3rd move:    2     1     2     2     2
#
#
# Example2
#
# Input: [0,3,0]
#
# Output: 2
#
# Explanation:
# 1st move:    0     1     2     0
# 2nd move:    1     2 --> 0    =>    1     1     1
#
#
# Example3
#
# Input: [0,2,0]
#
# Output: -1
#
# Explanation:
# It's impossible to make all the three washing machines have the same number
# of dresses.
#
#
#
#
# Note:
#
# The range of n is [1, 10000].
# The range of dresses number in a super washing machine is [0, 1e5].
#
#
#

# @lc code=start

# Trick:
# - compute the work (number of operation) done by each machine
# - if operations are done sequentially, total work would be
#   the sum of work for each machine
# - if operations are done in parallel, total work is the max
#
# (in the parallel case, one machine can transfer from two
#  neighbors in one operation)  
#
# This trick can be reused in problems when things are done
# in parallel. Don't focus on how operations are implemented, but
# on the work of each processor.

class Solution:
    def findMinMoves(self, machines):
        s = sum(machines)
        target, rem = divmod(s, len(machines))
        if rem != 0:
            return -1
        res = 0
        for i, m in enumerate(machines):
            l = sum(machines[:i])
            r = sum(machines[i+1:])
            if m == target:
                this_machine_operation = abs(r - l) // 2
            elif m < target:
                this_machine_operation = i * target - l + abs(m - target) 
            else:
                this_machine_operation = (l - i * target) + abs(m - target) 
            res = max(res, this_machine_operation)
        return res


# @lc code=end

