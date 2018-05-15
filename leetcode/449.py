#TAGS bst
# Trick we can re-build a bst from its preorder traversal

def insert(node, i):
    if node is None:
        return TreeNode(i)
    elif i <= node.val:
        return TreeNode(node.val, insert(node.left, i), node.right)
    else:
        return TreeNode(node.val, node.left, insert(node.right, i))

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def f(node):
          if node is not None:
            res.append(str(node.val))
            f(node.left)
            f(node.right)
        f(root)
        return ' '.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        res = None
        for i in data.split():
            i = int(i)
            res = insert(res, i)
        return res
                


