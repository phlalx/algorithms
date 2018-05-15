#
# Union-find
#
# Interface:
# create : int -> t  represents set [0, n)
# find : t -> int -> int returns a representent of the equivalence class
# union : t -> int * int -> unit   merges two equivalence classes
#
# count : t -> int   returns the number of equivalence classes
#
# Forest, union by rank (try to minimize the height = rank of the tree)
# compressed path optimization
#
# O(n) for creation, O(1), O(1) amortized for other
# operations. This is the `right` implementation
#
# Two optimizations:
# 1. Try to keep tree small
# 2. Update pointers after a find
#

class UF:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [ 0 ] * n

def find(uf, i):
    if i == uf.p[i]:
        return i
    res = find(uf, uf.p[i])
    uf.p[i] = res  # optim
    return res

def union(uf, i, j):
    i, j = find(uf, i), find(uf, j)
    if i == j:
        return
    if uf.r[i] > uf.r[j]: # rank optim
        uf.p[j] = i
    else:  # rank optim
        uf.p[i] = j
        uf.r[j] = max(uf.r[j], 1 + uf.r[i])

N = 7
uf = UF(N)

union(uf, 0, 1)
union(uf, 2, 3)
union(uf, 4, 5)
union(uf, 0, 5)

for i in range(N):
    print(i, '->', find(uf, i))


