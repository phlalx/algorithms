#TAGS union find, cool

import string

class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        uf = {a:a for a in string.ascii_lowercase}
        
        def find(a):
            cur = a
            while cur != uf[cur]:
                cur = uf[cur]
            uf[a] = cur
            return cur
        
        def union(a, b):
            aa = find(a)
            bb = find(b)
            if aa == bb:
                return
            if aa > bb:
                uf[aa] = bb
            else:
                uf[bb] = aa
        
        for a, b in zip(A, B):
            union(a, b)
            
        return ''.join(find(c) for c in S)

        
