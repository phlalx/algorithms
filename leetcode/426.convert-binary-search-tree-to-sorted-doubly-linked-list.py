#TAGS dfs, bst
#cool, trick, don't be ashamed to use a nonlocal var in the recursive
# dfs
#
# walk the tree in order and keep track of previous node
#
# See also 530
#
# @lc app=leetcode id=426 lang=python3
#
# [426] Convert Binary Search Tree to Sorted Doubly Linked List
#
# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/
#
# algorithms
# Medium (53.98%)
# Likes:    496
# Dislikes: 54
# Total Accepted:    38.2K
# Total Submissions: 70.8K
# Testcase Example:  '{"$id":"1","val":4,"left":{"$id":"2","val":2,"left":{"$id":"4","val":1,"left":null,"right":null},"right":{"$id":"5","val":3,"left":null,"right":null}},"right":{"$id":"3","val":5,"left":null,"right":null}}'
#
# Convert a BST to a sorted circular doubly-linked list in-place. Think of the
# left and right pointers as synonymous to the previous and next pointers in a
# doubly-linked list.
#
# Let's take the following BST as an example, it may help you understand the
# problem better:
#
#
#
#
#
# We want to transform this BST into a circular doubly linked list. Each node
# in a doubly linked list has a predecessor and successor. For a circular
# doubly linked list, the predecessor of the first element is the last element,
# and the successor of the last element is the first element.
#
# The figure below shows the circular doubly linked list for the BST above. The
# "head" symbol means the node it points to is the smallest element of the
# linked list.
#
#
#
#
#
# Specifically, we want to do the transformation in place. After the
# transformation, the left pointer of the tree node should point to its
# predecessor, and the right pointer should point to its successor. We should
# return the pointer to the first element of the linked list.
#
# The figure below shows the transformed BST. The solid line indicates the
# successor relationship, while the dashed line means the predecessor
# relationship.
#
#
#
#
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
# Solution 1, using a global variable

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        dummy = Node(None, None, None)
        prev = dummy
        last = None

        def f(root):
            nonlocal prev, last
            if root is None:
                return
            f(root.left)

            root.left = prev
            prev.right = root

            prev = root
            last = root

            f(root.right)

        f(root)

        first = dummy.right
        if first:
            last.right = first
            first.left = last

        return first

# Tentative solution 2, local var
# doesn't work... when we unstack the recursive calls, we don't have
# the right value for prev
#
# class Solution:
#     def treeToDoublyList(self, root: 'Node') -> 'Node':
#         last = None

#         def f(root, prev):
#             nonlocal last
#             if root is None:
#                 return
#             f(root.left, prev)

#             root.left = prev
#             prev.right = root

#             last = root

#             f(root.right, root)

#         dummy = Node(None, None, None)
#         f(root, dummy)

#         first = dummy.right
#         if first:
#             last.right = first
#             first.left = last

#         return first

