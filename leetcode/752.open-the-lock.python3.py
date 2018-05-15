#TAGS bfs
#
# easy, just think of corner case
# TODO double-end bfs

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        
        def neighbors(state):
            l = [int(d) for d in state]
            for i in range(4):
                v = l[i]
                l[i] = (v + 1) % 10
                yield ''.join(str(u) for u in l)
                l[i] = (10 + v - 1) % 10
                yield ''.join(str(u) for u in l)
                l[i] = v
                
        init = '0000'
        to_visit = deque([init])
        seen = {init: 0}
        
        while to_visit:
            state = to_visit.popleft()
            if state == target:
                return seen[target]
            for neigh in neighbors(state):
                if neigh not in seen and neigh not in deadends:
                    to_visit.append(neigh)
                    seen[neigh] = seen[state] + 1
                    
        return -1
                    
            
        
