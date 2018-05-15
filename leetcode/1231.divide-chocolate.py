#tags binary search

# return first k such that p[k], else j+1
def binary_search(p, i, j):
    while i < j:
        m = (i + j) // 2
        if p(m):
            j = m
        else:
            i = m+1
    return i if p(i) else i + 1

class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        def is_possible_sweetness(x):
            cut = 0
            cur = 0
            for s in sweetness:
                cur += s
                if cur >= x:
                    cut += 1
                    cur = 0
            return not cut >= K + 1
        
        return binary_search(is_possible_sweetness, 0, sum(sweetness)) - 1
        
                
                
                
        
        
