class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        def f(node):
            if node is None:
                return ('full', -1)
            else:
                s, l = f(node.left)
                ss, ll = f(node.right)
                if s == 'full' and ss == 'full' and l == ll:
                    return ('full', l + 1)
                elif s == 'full' and ss == 'full' and l == ll + 1:
                    return ('complete', l + 1)
                elif s == 'full' and ss == 'complete' and l == ll:
                    return ('complete', l + 1)
                elif s == 'complete' and ss == 'full' and l == ll + 1:
                    return ('complete', l + 1)
                else:
                    return ('incomplete', None)
        return f(root)[0] in {'complete', 'full'}

        
