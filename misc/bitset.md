# bitset

We want to represent a set of N bits [ 0 1 ... (N - 1) ]
ALL = (1 << N) - 1 = 0b111..11
1 << N = 2 ** N
bit number i 1 << i
Iterating over all sets
for bits in range(ALL + 1):


def ispowerof2(n):
    return n >= 1 and (n & (n - 1)) == 0


# Femwick

```
def left(x):
    return x - (x & (-x))

def parent(x):
    return x + (x & (-x))
```

LSB: x & (-x)

Remember  -0011001100
         = 1100110111    almost the negation, except for the first 1 bits