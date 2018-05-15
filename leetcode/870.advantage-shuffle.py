#
# @lc app=leetcode id=870 lang=python3
#
# [870] Advantage Shuffle
#
# https://leetcode.com/problems/advantage-shuffle/description/
#
# algorithms
# Medium (43.21%)
# Likes:    378
# Dislikes: 23
# Total Accepted:    16.3K
# Total Submissions: 36.8K
# Testcase Example:  '[2,7,11,15]\n[1,10,4,11]'
#
# Given two arrays A and B of equal size, the advantage of A with respect to B
# is the number of indices i for which A[i] > B[i].
#
# Return any permutation of A that maximizes its advantage with respect to
# B.
#
#
#
#
# Example 1:
#
#
# Input: A = [2,7,11,15], B = [1,10,4,11]
# Output: [2,11,7,15]
#
#
#
# Example 2:
#
#
# Input: A = [12,24,8,32], B = [13,25,32,11]
# Output: [24,32,8,12]
#
#
#
#
# Note:
#
#
# 1 <= A.length = B.length <= 10000
# 0 <= A[i] <= 10^9
# 0 <= B[i] <= 10^9
#
#
#
#
#
#TAGS permutation, arrays
# Trick: we suppose B is sorted
# then we apply to A the inversion of the permutation
# used to sort B
# TODO better solution?

# @lc code=start
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        invert = sorted(range(n), key=B.__getitem__)  # pythoni
        B.sort()

        A.sort()
        j = n - 1
        i = 0
        res = [ None ] * n
        for k in reversed(range(n)):
            bk = B[k]
            if bk < A[j]:
                res[k] = A[j]
                j -= 1
            else:
                res[k] = A[i]
                i += 1

        res = sorted(enumerate(res), key=lambda x: invert[x[0]])
        return [ y for x,y in res ]


# @lc code=end

