#TAGS dp
#
# TODO redo, understand the trick, and improve this solution

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def best(nums, i, j):
    if i == j:
        return Node(nums[i])
    else:
        best_val = float('-inf')
        best_tree = None
        for k in range(i, j):
            tree1 = best(nums, i, k)
            tree2 = bla(nums, k+1, j)
            new_best = tree1.val / (tree2.val * 1.0)
            if new_best > best_val:
                best_tree = Node(new_best, tree1, tree2)
                best_val = new_best
        return best_tree

def bla(nums, i, j):
    if i == j:
        return Node(nums[i])
    else:
        best_val = float('inf')
        best_tree = None
        for k in range(i, j):
            tree1 = bla(nums, i, k)
            tree2 = best(nums, k+1, j)
            new_best = tree1.val / (tree2.val * 1.0)
            if new_best < best_val:
                best_tree = Node(new_best, tree1, tree2)
                best_val = new_best
        return best_tree

def to_string(tree, need_par):
    if tree.left is None:
        assert tree.right is None
        return str(tree.val)
    else:
        s1 = to_string(tree.left, False)
        s2 = to_string(tree.right, True)
        if need_par:
            return '(' + s1 + '/' + s2 + ')'
        else:
            return s1 + '/' + s2

class Solution:
    def optimalDivision(self, nums):
        tree = best(nums, 0, len(nums)-1)
        return to_string(tree, False)

def test():
    test_case = [2, 3, 4]
    res = Solution().optimalDivision(test_case)
    print(res)