#
# @lc app=leetcode id=272 lang=python3
#
# [272] Closest Binary Search Tree Value II
#
# https://leetcode.com/problems/closest-binary-search-tree-value-ii/description/
#
# algorithms
# Hard (50.12%)
# Likes:    610
# Dislikes: 20
# Total Accepted:    56.4K
# Total Submissions: 112.6K
# Testcase Example:  '[4,2,5,1,3]\n3.714286\n2'
#
# Given a non-empty binary search tree and a target value, find k values in the
# BST that are closest to the target.
#
# Note:
#
#
# Given target value is a floating point.
# You may assume k is always valid, that is: k ≤ total nodes.
# You are guaranteed to have only one unique set of k values in the BST that
# are closest to the target.
#
#
# Example:
#
#
# Input: root = [4,2,5,1,3], target = 3.714286, and k = 2
#
# ⁠   4
# ⁠  / \
# ⁠ 2   5
# ⁠/ \
# 1   3
#
# Output: [4,3]
#
# Follow up:
# Assume that the BST is balanced, could you solve it in less than O(n) runtime
# (where n = total nodes)?
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#TAGS bst, merge
#
# Simple solution: linearize and use merge sort over list of values

import bisect

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:

        vals = []

        def f(root):
            if root is None:
                return
            f(root.left)
            vals.append(root.val)
            f(root.right)

        f(root)

        i = bisect.bisect_left(vals, target)

        res = []
        n = len(vals)

        j = i
        i -= 1

        while i >= 0 and j < n and k > 0:
            a = vals[i]
            b = vals[j]
            assert target - a >= 0 and b - target >= 0
            if target - a < b - target:
                res.append(a)
                i -= 1
            else:
                res.append(b)
                j += 1
            k -= 1
        while i >= 0 and k > 0:
            res.append(vals[i])
            i -= 1
            k -= 1
        while j < n and k > 0:
            res.append(vals[j])
            j += 1
            k -= 1
        return res

# Better solution
#
# Take away: pred, succ in bst, k closest elements, search element in BST
#

def succ(tree):
    if tree.right:
        tree = tree.right
        while tree.left is not None:
            tree = tree.left
    else:
        while tree.parent is not None and tree.parent.left != tree:
            tree = tree.parent
        tree = tree.parent
    return tree

def pred(tree):
    if tree.left:
        tree = tree.left
        while tree.right is not None:
            tree = tree.right
    else:
        while tree.parent is not None and tree.parent.right != tree:
            tree = tree.parent
        tree = tree.parent
    return tree

# What element do we return if the target isn't in the tree?
# Can be the element just before or just after.
#
def search(tree, v):
    if v < tree.val and tree.left:
        return search(tree.left, v)
    elif v > tree.val and tree.right:
            return search(tree.right, v)
    else:
        assert tree is not None
        return tree

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:

        def f(root, parent):
            if root is None:
                return
            root.parent = parent
            f(root.left, root)
            f(root.right, root)

        f(root, None)

        node = search(root, target)
        if node.val <= target:
            left = node
            right = succ(node)
        else:
            left = pred(node)
            right = node

        res = []
        while left and right and k > 0:
            if target - left.val < right.val - target:
                res.append(left.val)
                left = pred(left)
                k -= 1
            else:
                res.append(right.val)
                right = succ(right)
                k -= 1
        while left and k > 0:
            res.append(left.val)
            left = pred(left)
            k -= 1
        while right and k > 0:
            res.append(right.val)
            right = succ(right)
            k -= 1

        return res

# Same a before without changing the tree, but this is still not optimal
# we can compute all successors/predecessors in one go
# REDO

def succ(tree, node):
    # potential successor, actual successor if the node doesn't have a right child
    parent = None  
    while node is not tree:
        if node.val < tree.val:
            parent = tree
            tree = tree.left
        else:
            tree = tree.right
    if tree.right:
        tree = tree.right
        while tree.left is not None:
            tree = tree.left
        return tree
    return parent

def pred(tree, node):
    # potential predecessor, actual successor if the node doesn't have a right child
    parent = None
    while node is not tree:
        if node.val < tree.val:
            tree = tree.left
        else:
            parent = tree
            tree = tree.right
    if tree.left:
        tree = tree.left
        while tree.right:
            tree = tree.right
        return tree
    return parent
    
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:

        node = search(root, target)
        if node.val <= target:
            left = node
            right = succ(root, node)
        else:
            left = pred(root, node)
            right = node

        res = []
        while left and right and k > 0:
            if target - left.val < right.val - target:
                res.append(left.val)
                left = pred(root, left)
                k -= 1
            else:
                res.append(right.val)
                right = succ(root, right)
                k -= 1
        while left and k > 0:
            res.append(left.val)
            left = pred(root, left)
            k -= 1
        while right and k > 0:
            res.append(right.val)
            right = succ(root, right)
            k -= 1

        return res

# Other method could use a next element iterator see 173: O(log n) space,
# but amortized O(1) pred/succ.


# An other cool solution based on a sliding window. We keep a dequeue of
# sorted elements of size k 

# Take away/trick: maintaing sliding window while walking a tree
from collections import deque

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:

        d = lambda x,y: abs(x - y)

        window = deque()
        def f(node):
            if node is None:
                return

            f(node.left)

            window.append(node.val)
            if len(window) == k + 1:
                if d(window[0], target) < d(window[-1], target):
                    window.pop()
                else:
                    window.popleft()
            f(node.right)

        f(root)
        return list(window)


# @lc code=end

