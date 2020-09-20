#TAGS simple bfs

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins.sort()
        def neighbors(amount):
            for c in coins:
                if amount - c < 0:
                    break
                yield amount - c
    
        to_visit = deque([amount])
        seen = {amount: 0}
        while to_visit:
            amount = to_visit.popleft()
            if amount == 0:
                return seen[amount]
            for neigh in neighbors(amount):
                if neigh in seen:
                    continue
                seen[neigh] = seen[amount] + 1
                to_visit.append(neigh)
        return -1
        
        
