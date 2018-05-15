#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#
# https://leetcode.com/problems/buddy-strings/description/
#
# algorithms
# Easy (27.84%)
# Likes:    447
# Dislikes: 287
# Total Accepted:    39.6K
# Total Submissions: 143.2K
# Testcase Example:  '"ab"\n"ba"'
#
# Given two strings A and B of lowercase letters, return true if and only if we
# can swap two letters in A so that the result equals B.
#
#
#
# Example 1:
#
#
#
# Input: A = "ab", B = "ba"
# Output: true
#
#
#
# Example 2:
#
#
# Input: A = "ab", B = "ab"
# Output: false
#
#
#
# Example 3:
#
#
# Input: A = "aa", B = "aa"
# Output: true
#
#
#
# Example 4:
#
#
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
#
#
#
# Example 5:
#
#
# Input: A = "", B = "aa"
# Output: false
#
#
#
#
# Note:
#
#
# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A and B consist only of lowercase letters.
#
#
#
#
#
#
#
#
#TAGS array, implem
# simple but careful with corner cases
#  abc, abc returns False
#  abb, abb returns True

# @lc code=start
class Solution:
    # def buddyStrings(self, A: str, B: str) -> bool:
    #     n = len(A)
    #     if len(B) != n:
    #         return False
    #     i = 0
    #     while i < n and A[i] == B[i]:
    #         i += 1
    #     if i == n:  # A and B are equal
    #         return len(set(A)) != n  # we need at least one duplicate
    #     a = i
    #     i += 1
    #     while i < n and A[i] == B[i]:
    #         i += 1
    #     if i == n :
    #         return False
    #     b = i
    #     if not (A[a] == B[b] and A[b] == B[a]):
    #         return False
    #     return A[i+1:] == B[i+1:]
        
    # Same idea with indices
    # find the first two unequals pairs A[i], B[i]
    # there can't be more than two
    def buddyStrings(self, A: str, B: str) -> bool:
        n = len(A)
        if len(B) != n:
            return False
        a = None
        b = None
        for u, v in zip(A, B):
            if u != v:
                if a is None:
                    a = u, v
                elif b is None:
                    b = u, v
                else:
                    return False
        if a is None and b is None:
            return len(set(A)) != n
        elif b is None:
            return False
        else:
            return (a[0], a[1]) == (b[1], b[0])

        

        
        


# @lc code=end

