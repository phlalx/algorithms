#TAGS tree
# pretty cool
#
# everything follows from this diagram
# V prefix(A) prefix(B)
# infix(A) V infix(B)
#
# consume pre as they come, but need to "bound" the infix part for
# the recursion to work
# 

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        pre = iter(preorder)
        def f(i, j):
            if i == j:
                return None
            else:
                v = next(pre)
                iv = inorder.index(v)
                return TreeNode(v, f(i, iv), f(iv+1, j))
        n = len(inorder)
        return f(0, n)
