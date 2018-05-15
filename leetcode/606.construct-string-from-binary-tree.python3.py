# TAGS binary tree, string
# TODO factorize code in cases


def walk(t, res, par):
    if par:
        res.append("(")

    if t is None:
        pass
    elif t.right is None and t.left is None:
        res.append(str(t.val))
        pass
    elif t.right is None:
        res.append(str(t.val))
        walk(t.left, res, True)
    else:
        res.append(str(t.val))
        walk(t.left, res, True)
        walk(t.right, res, True)

    if par:
        res.append(")")


class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        res = []
        walk(t, res, False)
        return "".join(res)
