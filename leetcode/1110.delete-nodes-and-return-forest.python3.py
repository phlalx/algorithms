# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#TAGS bst dfs
#
# regular dfs with keeping track of closest non deleted parent
#
# return all nodes which aren't deleted and which parent is deleted
# Also keep track of parent in order to remove deleted node from the tree
#

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        s = set(to_delete)
        res = []
        def f(node, parent, deleted):
            if node is None:
                return
            cur_deleted = node.val in s
            if cur_deleted and not deleted:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
            if not cur_deleted and deleted:
                res.append(node)            
            f(node.left, node, cur_deleted)
            f(node.right, node, cur_deleted)

        f(root, None, True)
        return res
        
