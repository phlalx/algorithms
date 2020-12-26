#TAGS tree kadane
# generalize kadane on a tree, cool
# easy if you see the proper recurrence relation
# we only need to compute recursively the max array going downward for
# each node. From deduce the result from there
# Trick: we could use a "global" variable to store the final result

from typing import Tuple

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def f(node) -> Tuple[int, int]:
            # max path from root (possibly empty), max path overall
            if node is None:
                return 0, float('-inf')
            l, ll = f(node.left)
            r, rr = f(node.right)
            a = max(0, l + node.val, r + node.val) 
            path_through_root = max(node.val + l, node.val + r, node.val + l + r)
            aa = max(ll, rr, path_through_root)
            return a, aa
        _, a = f(root)
        return a

# Trick: we use a "global" variable to store the final result
# class Solution:
#     def maxPathSum(self, root: TreeNode) -> int:
#         best = float('-inf')
#         def dfs(node):
#             nonlocal best
#             if node is None:
#                 return 0
#             lpath = dfs(node.left)
#             rpath = dfs(node.right)
#             path = node.val + max(0, lpath, rpath)
#             best = max(best, node.val + max(0, lpath, rpath, lpath + rpath))
#             return path
#         dfs(root)
#         return best