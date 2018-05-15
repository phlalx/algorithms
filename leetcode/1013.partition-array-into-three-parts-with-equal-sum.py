#
# @lc app=leetcode id=1013 lang=python3
#
# [1013] Partition Array Into Three Parts With Equal Sum
#
# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/description/
#
# algorithms
# Easy (56.25%)
# Likes:    296
# Dislikes: 49
# Total Accepted:    27.4K
# Total Submissions: 48.6K
# Testcase Example:  '[0,2,1,-6,6,-7,9,1,2,0,1]'
#
# Given an array A of integers, return true if and only if we can partition the
# array into three non-empty parts with equal sums.
#
# Formally, we can partition the array if we can find indexes i+1 < j with
# (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1]
# + ... + A[A.length - 1])
#
#
# Example 1:
#
#
# Input: A = [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
#
#
# Example 2:
#
#
# Input: A = [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false
#
#
# Example 3:
#
#
# Input: A = [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
#
#
#
# Constraints:
#
#
# 3 <= A.length <= 50000
# -10^4 <= A[i] <= 10^4
#
#
#

# @lc code=start
#TAGS dp
# see 473, 698
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        x = sum(A)
        q, r = divmod(x, 3)
        if r != 0:
            return False
        n = len(A)

        memo = {}
        # can split A[:i] in k parts of sum q
        def f(i, k):
            res = memo.get((i,k))
            if res is not None:
                return res
            if k == 0:
                res = i == -1
            else:
                cur = 0
                res = False
                while i >= 0:
                    cur += A[i]
                    i -= 1
                    if cur == q and f(i, k-1):
                        res = True
                        break
            memo[(i, k)] = res
            return res

        return f(n-1, 3)





# @lc code=end

