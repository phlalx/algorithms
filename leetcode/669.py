#TAGS tree

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def trim(node, L, R):
            if node is None:
                return None
            elif node.val < L:
                return trim(node.right, L, R)
            elif node.val > R:
                return trim(node.left, L, R)
            else:
                node.left = trim(node.left, L, R)
                node.right =  trim(node.right, L, R)
                return node
        return trim(root, L, R)
