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
# Simplest implementation based on forest
# Remember: interface and enough to maintain a parent array
#
# Init O(1)
# Find O(n)
# Union O(n)

def init(n):
    return list(range(n))

def find(uf, i):
    while i != uf[i]:
        i = uf[i]
    return i

def union(uf, i, j):
    i, j = find(uf, i), find(uf, j)
    assert i != j
    uf[i] = j

N = 7
uf = init(N)

union(uf, 0, 1)
union(uf, 2, 3)
union(uf, 4, 5)
union(uf, 0, 5)

for i in range(N):
    print(i, '->', find(uf, i))


