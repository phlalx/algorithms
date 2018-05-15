# Intersection
# List with no duplicate elements


# Naive implementation
# O(n.p)

# Sorted input, similar to merging in merge sort
# Space = O(1) (+ output)
# Time = O(min(n, p))

def inter(a, b):
    n = len(a)
    p = len(b)
    i = 0
    j = 0
    res = []
    while i < n and j < p:
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            res.append(a[i])
            i += 1
            j += 1

    return res

a = [1, 2, 7, 8]
b = [7, 8, 9]
assert inter(a, b) == [7, 8]

# If inputs aren't sorted
# We can re-use `inter` and add a sorting phase
# Space = O(1) + output
# Time = n.log(n) + p.log(p) + min(n, p)

# We can also sort only one array (p), and binary search all elements
# Space = O(1)
# Time = (n + p) * min(log(p), log(n))


# Using two sets
# Space = O(n + p) (hash set)
# Time = O(n + p)

def inter(a, b):
    aa = set(a)  # O(n)
    bb = set(b)  # O(p)
    aa.intersection_update(bb)
    return list(aa)

assert sorted(inter(a, b)) == [7, 8]

# Using one set
# Time O(n + p)  # n for constructing aa, p for going through b
# Space O(n))
# We can switch a and b to minimize space
def inter(a, b):
    aa = set(a)  # O(n)
    return [e for e in b if e in aa]

assert sorted(inter(a, b)) == [7, 8]

# We don't have tree sets in python, but there would be no reason to use them
# because we don't need to add elements dynamically. Sorted array has the same
# cost (construction and lookup)
