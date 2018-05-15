# Femwick a.k.a binary indexed tree
#
# Simple to understand with graph
#  -----------------------
#  ------------
#  ----        ----
#  -     -     -     -  -
#  1  2  3  4  5  6  7  8
#
#  left(1) = 0   # remove least significant bit
#  left(2) = 0
#  left(3) = 2
#  left(4) = 0
#  left(5) = 4
#  ...
#
# Need to remember that left(i) =  i  - (i ~ -i)
# and parent(i) =  i  + (i ~ -i)

# Remember
# . we build a segment tree
# . tree is stored as an array t of nodes of the same size as the initial array
#   => indexed tree
# . each node represents an interval
#  (* why interval never overlap (only full inclusion) *)
# . t[i] = sum of elements in interval [i - left(i) + 1, i]
#      singleton if i is odd, and [1, i] if i = 2 ** k
# . function left, substracts least significant 1 bit.
#                   If left(x) == 0, no left neighbor
#
# TODO update

s = [None, 6, 1, 2, 3, 5]

def left(x):
    return x - (x & (-x))

def parent(x):
    return x + (x & (-x))

class Femwick:

    def __init__(self, s):
        n = len(s)
        self.t = [ 0 ] * n
        cur = 0
        for i in range(1, n):
            cur += s[i]
            self.t[i] = cur - self.t[left(i)]

    def update(self, i, v):
        incr = v - s[i]
        s[i] = v
        while i < len(self.t):
            self.t[i] += incr
            assert parent(i) > i
            i = parent(i)

    def add(self, k):
        res = 0
        i = k
        while i > 0:
            res += self.t[i]
            i = left(i)
        assert res == sum(s[1:k+1])
        return res

f = Femwick(s)

for i in range(1, len(s)):
    print(f.add(i))

f.update(2, 10)

# s = [None, 6, 10, 2, 3, 5]
print()
for i in range(1, len(s)):
    print(f.add(i))

