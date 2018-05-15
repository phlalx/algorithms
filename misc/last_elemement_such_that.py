# Common patterns

# last element such that P(x)

ar = [1, 3, 0, 4, 5]

# Just look the first element s.t. not P(x)
# and substract 1

def P(x, l):
    return x <= l

def f(ar, l):
    i = 0
    n = len(ar)
    while i < n and P(ar[i], l):
        i += 1
    return i - 1

assert f(ar, 0) == -1
assert f(ar, 5) == 4
assert f(ar, 2) == 0
assert f(ar, 8) == 4
assert f(ar, -3) == -1

# smallest sub-sum such that ss <= x

def f(ar, l):
    i = 0
    n = len(ar)
    cur_sum = 0
    while i < n and cur_sum <= l:
        cur_sum += ar[i]
        i += 1
    return sum(ar[:i-1])

assert f(ar, 5) == 4 

