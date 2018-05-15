#TAGS cool, BST
# 493

# merge  sort
https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76584/Mergesort-solution

# Very clever use of Femwick tree
https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76657/3-ways-(Segment-Tree-Binary-Indexed-Tree-Binary-Search-Tree)-clean-python-code

# We use an augmented BST to retrieve the number of elements lower than a
# given value. This should be O(n.log(n)) with a balanced BST.
#
# TODO use a better data structure, femwick tree?

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.nums = 1  # number of element smaller than val in this subtree

def insert(node, val):
    if node is None:
        return Node(val)
    if val <= node.val:
        node.nums += 1
        node.left = insert(node.left, val)
    else:
        node.right = insert(node.right, val)
    return node

def num_of_elts_less(node, val):
    if node is None:
        return 0
    elif val <= node.val:
        return num_of_elts_less(node.left, val)
    else:
        return node.nums + num_of_elts_less(node.right, val)

class Solution:
    def countSmaller(self, nums):
        tree = None
        res = []
        for v in reversed(nums):
            tree = insert(tree, v)
            res.append(num_of_elts_less(tree, v))
        return reversed(res)

# TODO try to use femwick or segment tree

# TODO simplest way:
#  compute for each number the number of numbers that cross it going
# from left to right in a stable start.
# "augmented" merge sort.