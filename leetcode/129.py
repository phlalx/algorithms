#TAGS tree

# TODO do we need to stop the recursion before None?
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, cur):
            nonlocal res
            if not node.left and not node.right:
                res += 10 * cur + node.val
                return
            cur = 10 * cur + node.val
            if node.left:
                dfs(node.left, cur)
            if node.right:
                dfs(node.right, cur)
        if root is None:
            return 0
        dfs(root, 0)
        return res
