# TAGS tree
# Better solutions https://en.wikipedia.org/wiki/Cartesian_tree


def build(nums, i, j):
    if i == j:
        return None
    m, k = max(((nums[k], k) for k in range(i, j)))
    t = TreeNode(m)
    t.left = build(nums, i, k)
    t.right = build(nums, k + 1, j)
    return t


class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        assert nums
        return build(nums, 0, len(nums))
