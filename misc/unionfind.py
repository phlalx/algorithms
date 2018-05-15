#
# Union-find
#
# Useful to compute equivalence-classes.
# connex components of a graph
# Kruskal (Mnemotechnique tip   KrUUUskal, U like union find) Elog(E) = Elog(V)
#
# Interface:
# create : int -> t  represents set [0, n)
# find : t -> int -> int returns a representent of the equivalence class
# union : t -> int * int -> unit   merges two equivalence classes
# (count : t -> int    returns the number of equivalence classes)
#
#
# Application : Prim, Kruskal?
#
# Naive implementation based on lists. Not interesting, slow and not
# simpler to program. First implem in Cormen.
#
# Complexity
# creation = O(n)
# find = O(1)
# union = O(n)  find two representants O(1) + merge O(n)

class bucket:

    def __init__(self, val):
        self.first = val
        self.last = val
        self.num = 1

class cell:

    def __init__(self, val):
        self.val = val
        self.succ = None
        self.first = None

def init(n):
    res = [ None ] * n
    for i in range(n):
        c = cell(i)
        c.first = c
        res[i] = bucket(c)
    return res

def find(uf, i):
    return uf[i].first.first.val

def union_naive(uf, i, j):
    uf[i].last.succ = uf[j].first
    uf[i].last = uf[j].last
    uf[i].num += uf[j].num
    cur = uf[j].first
    while cur:
        cur.first = uf[i].first
        cur = cur.succ

# we append the smallest list to the bigger one
def union(uf, i, j):
    print('union', i, j)
    i, j = find(uf, i), find(uf, j)
    assert i != j
    if uf[i].num > uf[j].num:
        union_naive(uf, i, j)
    else:
        union_naive(uf, j, i)

N = 7
uf = init(N)

union(uf, 0, 1)
union(uf, 2, 3)
union(uf, 4, 5)
union(uf, 0, 5)

for i in range(N):
    print(i, '->', find(uf, i))


