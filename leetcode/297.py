#TAGS tree, dfs

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def f(node):
          if node is None:
            res.append('*')
          else:
            f(node.left)
            f(node.right)
            res.append(str(node.val))
        f(root)
        return ' '.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        st = []
        for token in data.split():
          if token is '*':
            st.append(None)
          else:
            right = st.pop()
            left = st.pop()
            st.append(TreeNode(int(token), left, right))
        assert len(st) == 1
        return st[0]
        
