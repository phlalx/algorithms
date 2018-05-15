# ARITHMETIC

# O(log(n))
def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def primes(n):
    assert n >= 1
    res = []
    f = 2
    while n > 1:
        while n % f == 0:
            res.append(f)
            n //= f
        f += 1
    return res

# O(n.log(log(n)), so essentially linear.
# this relies on: 1/2 + 1/3 + 1/5 + ... 1 / P_n ~ ln(ln(n))
def sieve(n):
    # list of positive number, easier to include 0 and 1, so we avoid
    # using offsets
    num = [False, False] + [True] * (n-2)
    i = 2
    res = []
    while i * i < len(num): # no need to go from i to len(num)
        if not num[i]:
            i += 1
            continue
        # little trick here, no need to consider 2i, 3i, .. k.i for k < i
        # because there were already discarded
        j = i * i
        while j < len(num):
            num[j] = False
            j += i
        i += 1

    return [ i for i, v in enumerate(num) if v ]
