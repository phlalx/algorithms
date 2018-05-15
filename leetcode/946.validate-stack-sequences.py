#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#
# https://leetcode.com/problems/validate-stack-sequences/description/
#
# algorithms
# Medium (60.36%)
# Likes:    647
# Dislikes: 19
# Total Accepted:    37.3K
# Total Submissions: 61.9K
# Testcase Example:  '[1,2,3,4,5]\n[4,5,3,2,1]'
#
# Given two sequences pushed and popped with distinct values, return true if
# and only if this could have been the result of a sequence of push and pop
# operations on an initially empty stack.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
# 
# 
# 
# Example 2:
# 
# 
# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= pushed.length == popped.length <= 1000
# 0 <= pushed[i], popped[i] < 1000
# pushed is a permutation of popped.
# pushed and popped have distinct values.
# 
# 
# 
#
# TAGS stack

# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        n = len(pushed)
        st = []
        for v in popped:
            if st and st[-1] == v:
                st.pop()
            else:
                while i < n and pushed[i] != v:
                    st.append(pushed[i])
                    i += 1
                if i == n:
                    return False
                else:
                    i += 1
        return st == [] and i == n

# @lc code=end

