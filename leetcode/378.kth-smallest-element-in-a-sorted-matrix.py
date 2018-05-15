#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (50.55%)
# Likes:    1425
# Dislikes: 89
# Total Accepted:    126.6K
# Total Submissions: 250.3K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# Given a n x n matrix where each of the rows and columns are sorted in
# ascending order, find the kth smallest element in the matrix.
#
#
# Note that it is the kth smallest element in the sorted order, not the kth
# distinct element.
#
#
# Example:
#
# matrix = [
# ⁠  [ 1,  5,  9],
# ⁠  [10, 11, 13],
# ⁠  [12, 13, 15]
# ],
# k = 8,
#
# return 13.
#
#
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ n^2.
#

# TAGS k-merge
# see 373, 668
# TODO seems we don't use the fact that both lines and cols are sorted...
# @lc code=start
# trick: remember that merge is also good to find k-th element
#

import heapq

class Solution:

  def kthSmallest(self, matrix, k):
    n = len(matrix)
    p = len(matrix[0])
    heap = [ (matrix[0][j], 0, j) for j in range(p) ]
    heapq.heapify(heap)
    for _ in range(k):
      v, i, j = heapq.heappop(heap)
      if i + 1 < n:
        heapq.heappush(heap, (matrix[i+1][j], i+1, j))
    return v


# @lc code=end

