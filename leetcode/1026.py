#TAG tree
# easy, but can do better
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        res = float('-inf')
        def f(node) -> Tuple[int, int]:  # max, min in subtree
            nonlocal res
            if node is None:
                return float('-inf'), float('inf')
            lmax, lmin = f(node.left)
            rmax, rmin = f(node.right)
            ma, mi = max(node.val, lmax, rmax), min(node.val, lmin, rmin)
            res = max(res, abs(node.val - ma), abs(node.val - mi))
            return ma, mi

# nicer solution top-down
class Solution:
    def maxAncestorDiff(self, node: TreeNode) -> int:
        if node is None:
            return 0
        def f(node, ma, mi):
            if node is None:
                return ma - mi
            else:
                ma = max(node.val, ma)
                mi = min(node.val, mi)
                res = max(f(node.left, ma, mi), f(node.right, ma, mi))
                return res
        return f(node, float('-inf'), float('inf'))
