#TAGS median, bst, kselect
#
# TODO implement either a priority queue with removal or an ordered set
#      structure
#
# see also 295
#
# @lc app=leetcode id=480 lang=python3
#
# [480] Sliding Window Median
#
# https://leetcode.com/problems/sliding-window-median/description/
#
# algorithms
# Hard (33.62%)
# Likes:    493
# Dislikes: 52
# Total Accepted:    30.5K
# Total Submissions: 90.8K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# Median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value. So the median is the mean of the two
# middle value.
# Examples:
# [2,3,4] , the median is 3
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position. Your
# job is to output the median array for each window in the original array.
#
# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
#
#
# Window position                Median
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       1
# ⁠1 [3  -1  -3] 5  3  6  7       -1
# ⁠1  3 [-1  -3  5] 3  6  7       -1
# ⁠1  3  -1 [-3  5  3] 6  7       3
# ⁠1  3  -1  -3 [5  3  6] 7       5
# ⁠1  3  -1  -3  5 [3  6  7]      6
#
#
# Therefore, return the median sliding window as [1,-1,-1,3,5,6].
#
# Note:
# You may assume k is always valid, ie: k is always smaller than input array's
# size for non-empty array.
#

from typing import List

def median(val):
    n = len(val)
    if n % 2 == 0:
        return (val[(n-1) // 2] + val[(n-1) // 2 + 1]) / 2.0
    else:
        return val[(n-1) // 2]

class Solution:

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)
        res = []
        val = nums[:k]
        val.sort()
        res.append(median(val))

        for i in range(k, n):
            j = val.index(nums[i - k])
            val[j] = nums[i]
            val.sort()
            res.append(median(val))

        return res

#
# from typing import List
# from collections import deque

# # Deletion for augmented BST is hard... lot of bugs
# # hard to debug because lack of visual information on the trace (parent
# # pointers, size)
# #
# # next time, add more assertions

# class Node:

#     def __init__(self, v):
#         self.v = v
#         self.left = None
#         self.right = None
#         self.size = 1
#         self.p = None


# # Remove root node from tree, preserve existing node
# # res.p isn't specified
# def remove_root(tree):
#     assert tree is not None
#     if tree.left is None:
#         return tree.right
#     elif tree.right is None:
#         return tree.left
#     else:
#         # BUG not deleting the node, just the value
#         # tree.v = tree.left.v
#         # tree.left = remove_root(tree.left)
#         # tree.size -= 1

#         # Correct solution
#         # tree.left will become the new root

#         res = tree.left
#         res.left = remove_root(tree.left)
#         res.size = tree.size - 1
#         res.right = tree.right
#         if res.left:
#             res.left.p = res
#         if res.right:
#             res.right.p = res
#         return res


# def remove(tree, n):
#     if tree == n:
#         res = remove_root(tree)
#         res.p = None
#         return res
#     p = n.p
#     new_n = remove_root(n)
#     if new_n is not None:
#         new_n.p = p
#     if p.left == n:
#         p.left = new_n
#     else:
#         assert p.right == n
#         p.right = new_n
#     while p is not None:
#         p.size -= 1
#         p = p.p
#     return tree

# def tree_to_string(tree):
#     if tree is None:
#         return ''
#     else:
#         return f'({tree.v}-{tree.size} *{tree_to_string(tree.left)}* *{tree_to_string(tree.right)}*)'

# def insert(tree, n):
#     if tree is None:
#         n.p = None
#         return n
#     if n.v < tree.v:
#         tree.left = insert(tree.left, n)
#         tree.left.p = tree
#     else:
#         tree.right = insert(tree.right, n)
#         tree.right.p = tree
#     tree.size += 1
#     assert tree is not None
#     return tree

# def select(tree, k):
#     assert tree is not None
#     # a is the index of tree.v in the sorted array representation of tree
#     a = 0 if tree.left is None else tree.left.size
#     if k == a:
#         res = tree.v
#     elif k < a:
#         res = select(tree.left, k)
#     else:
#         res = select(tree.right, k - a - 1)
#     print(f'select {k} in {tree_to_string(tree)} (size {tree.size}) is {res}')
#     return res

# def median(tree):
#     assert tree is not None
#     n = tree.size
#     if n % 2 == 1:
#         res = select(tree, n // 2)
#     else:
#         res = (select(tree, n // 2) + select(tree, (n // 2) - 1)) / 2.0
#     print(f'median is {res}')
#     return res

# class Solution:
#     def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
#         q = deque()
#         tree = None
#         for i, v in enumerate(nums[:k]):
#             n = Node(v)
#             q.append(n)
#             tree = insert(tree, n)
#             assert tree.size == i+1
#         res = []
#         res.append(median(tree))
#         for v in nums[k:]:
#             old_n = q.popleft()
#             n = Node(v)
#             q.append(n)
#             tree = insert(tree, n)
#             assert tree.size == k+1
#             print('insert', n.v, tree_to_string(tree))
#             tree = remove(tree, old_n)
#             print('remove', old_n.v ,tree_to_string(tree))
#             assert tree.size == k
#             res.append(median(tree))
#         return res
