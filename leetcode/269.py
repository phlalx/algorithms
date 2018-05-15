# TAGS topological sort
# TODO use khan

class Stop(Exception):
    pass

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = dict()
        for w in words:
            for c in w:
                adj[c] = set()
        
        for w, ww in zip(words, words[1:]):
            is_prefix = True
            for c, cc in zip(w, ww):
                if c != cc:
                    adj[c].add(cc)
                    is_prefix = False
                    break
               
            if is_prefix and len(ww) < len(w):
                return ''
        
        order = []
        seen = {c:0 for c in adj}

        def dfs(c:str):
            for cc in adj[c]:
                if seen[cc] == 1:
                    raise Stop
                elif seen[cc] == 2:
                    continue
                else:
                    seen[cc] = 1
                    dfs(cc)
            order.append(c)
            seen[c] = 2

        try:
            for c in list(adj):
                if seen[c] == 0:
                    seen[c] = 1
                    dfs(c)
                
            return ''.join(order)[::-1]
        except Stop:
            return ''
