#
# @lc app=leetcode id=247 lang=python3
#
# [247] Strobogrammatic Number II
#
# https://leetcode.com/problems/strobogrammatic-number-ii/description/
#
# algorithms
# Medium (45.24%)
# Likes:    276
# Dislikes: 88
# Total Accepted:    54.8K
# Total Submissions: 120.8K
# Testcase Example:  '2'
#
# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).
# 
# Find all strobogrammatic numbers that are of length = n.
# 
# Example:
# 
# 
# Input:  n = 2
# Output: ["11","69","88","96"]
# 
# 
#
#TAGS backtrack
#
# Take away:
#   took me some time to write form_result correctly
#   it was easier to define the array with the right size from the beginning
#   also, we can't know the right size just from cur, we need to pass parameter
#   n too...
#
#   In the backtracking function, don't try to be smart and just distinguish
#   between i = 0, i == middle and regular case.
#
#  This current solution is too slow... try different approach REDO

d = { '0':'0', '1':'1', '6':'9', '9':'6', '8':'8' }

def form_result(cur, n):
    # at least 1 digit
    k = len(cur)
    res = list(cur) + [None] * (n - k)
    assert len(res) == n
    for i in range(k):
        res[-i-1] = d[res[i]]
    return ''.join(res)
    
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 0:
            return []
        elif n == 1:
            return ['0', '1', '8']
        middle = (n - 1) // 2
        res = []
        def f(i, cur):
            if i == middle + 1:
                res.append( form_result(cur, n) )
            else:
                if i == 0:
                    digits = ['1', '6', '8', '9']
                elif i == middle and n % 2 == 1:
                    digits = ['0', '1', '8']
                else:
                    digits = list(d.keys())
                for v in digits:
                    cur.append(v)
                    f(i+1, cur)
                    cur.pop()
        f(0, [])
        return res




