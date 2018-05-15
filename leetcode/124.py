#TAGS tree
# easy
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
