# Think Femwick as a generalization of the prefix sums

t = [1,3,4,5]  # t start at 0, but t[0] correspond to bit[1]
               # (just like for prefix sums)
n = len(t)

# a bit is an array, similar to the array of prefix sums but
# each value represents the sum of a sub array of t

def lsb(i):
    return i & (-i)

# returns sum(t[:i])
def prefix_sum(i):
    res = 0
    while i > 0:
        res += bit[i]
        i -= lsb(i)
    return res

# we compute the bit array almost like the regular prefix_sum array
# we use the prefix_sum
bit = [ 0 ] * (n + 1)

cur = 0
for i in range(1, n+1):
    cur += t[i-1]
    bit[i] = cur -  prefix_sum(i - lsb(i))

def test():
    for i in range(n+1):
        assert prefix_sum(i) == sum(t[:i]), i

test()

# simulate an update t[i] = v
def update(i, v):
    j = i + 1
    while j < n + 1:
        bit[j] += v - t[i]  # add the increment to all interval containing t[i]
        j += lsb(i)  #  TODO I don't get this

t[2] = 4
update(2, 4)

test()

