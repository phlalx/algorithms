#
# @lc app=leetcode id=493 lang=python3
#
# [493] Reverse Pairs
#
# https://leetcode.com/problems/reverse-pairs/description/
#
# algorithms
# Hard (23.57%)
# Likes:    587
# Dislikes: 88
# Total Accepted:    27.6K
# Total Submissions: 117.1K
# Testcase Example:  '[1,3,2,3,1]'
#
# Given an array nums, we call (i, j) an important reverse pair if i < j and
# nums[i] > 2*nums[j].
#
# You need to return the number of important reverse pairs in the given array.
#
# Example1:
#
# Input: [1,3,2,3,1]
# Output: 2
#
#
# Example2:
#
# Input: [2,4,3,5,1]
# Output: 3
#
#
# Note:
#
# The length of the given array will not exceed 50,000.
# All the numbers in the input array are in the range of 32-bit integer.
#
#
#

#TAGS cool, divide and conquer, double pointer
# TODO beats 7%, still too slow
# See misc/product_pred.py
# 315, 327

# https://leetcode.com/problems/reverse-pairs/discuss/97268/General-principles-behind-problems-similar-to-%22Reverse-Pairs%22

# @lc code=start

def f(nums, i, j):
    assert 0 <= i <= j < len(nums)
    if i == j:
        return 0
    pred = lambda i, j: nums[i] > 2 * nums[j]
    m = (i + j) // 2
    res = f(nums, i, m) + f(nums, m+1, j)

    # Count elements that satisfy pred. O(n) because of monoticity of pred
    #        F   F
    #    T  (T)  F
    #        T
    #
    ii = m
    jj = j
    while ii >= i:
        while jj >= m+1:
            if pred(ii, jj):
                res += jj - m
                break
            jj -= 1
        ii -= 1

    ii = i
    jj = m+1

    merge = []
    while ii <= m and jj <= j:
        if nums[ii] < nums[jj]:
            merge.append(nums[ii])
            ii += 1
        else:
            merge.append(nums[jj])
            jj += 1
    merge.extend(nums[ii:m+1])
    merge.extend(nums[jj:j+1])

    nums[i:j+1] = merge
    return res

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        return f(nums, 0, len(nums) - 1)

# @lc code=end

