#TAGS dp, cool

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        seen = {}
        def copy(node):
            res = seen.get(node)
            if res is None:
                res = Node(node.val)
                seen[node] = res
                # trick: update seen before the recursive call!  
                res.neighbors = [copy(nn) for nn in node.neighbors]
            return res
        if node is None:
            return None
        return copy(node)
