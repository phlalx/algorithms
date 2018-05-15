
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

def list_to_tree(l, i):
    if i >= len(l) or l[i] is None:
        return None
    else:
        left = list_to_tree(l, 2 * i + 1)
        right = list_to_tree(l, 2 * i + 2)
        return TreeNode(l[i], left, right)

# useful operations on dicts

d = {}
d['toto'] = 1
d['toto'] # retrieves element, KeyError exception if not present
d.get('toto') # retrieves element, but None if not present ()
d.get('toto', 'tutu') # retrieves element, but 'tutu' if not present ()
d['toto'] = 2 # set element
d.setdefault('toto', 'tutu') # get + set d['toto'] to 'tutu' if not present
d.items() # iterator on k, v in dict
d.keys()
d.values()

# default value

count = {}
count[node.val] = count.get(node.val, 0) + 1

count = defaultdict(int)
count[node.val] += 1

# example: group anagrams in a set of string using variant of bucket sort
def group(strings):
  m = {}
  for s in strings:
    key = ''.join(sorted(s))
    l = m.setdefault(key, [])
    l.append(s)
  res = []
  for _, v in m.items():
    res.extend(v)
  return res

# Bytearray

class BitArray(object):
    def __init__(self, lenght):
        self.values = bytearray(b"\x00" * (lenght // 8 + (1 if lenght % 8  else 0)))
        self.lenght = lenght

    def __setitem__(self, index, value):
        value = int(bool(value)) << (7 - index % 8)
        mask = 0xff ^ (7 - index % 8)
        self.values[index // 8] &= mask
        self.values[index // 8] |= value

    def __getitem__(self, index):
        mask = 1 << (7 - index % 8)
        return bool(self.values[index // 8] & mask)

    def __len__(self):
        return self.lenght

    def __repr__(self):
        return "<{}>".format(", ".join("{:d}".format(value) for value in self))

# dealing with files
# no need to explicity close the file when using the 'with ... as' construct

with open('workfile') as f:
  read_data = f.read()

# +, - infinity
float('inf'), float('-inf')

# A cool decorator
# note the use of *args

def memoize(f):
    mem = dict()
    def g(*args):
        if args not in mem:
            mem[args] = f(*args)
        return mem[args]
    return g

@memoize
def fibo(x):
  if x == 0:
    return 1
  if x == 1:
    return 1
  else:
    return fibo(x-1) + fibo(x-2)

# iterators

# reversed, zip, enumerate, iter
# all return iterators, they rely on methods of the objects they are applied too
# e.g. reversed need a __reversed__ methods or a __getitem__, __len__
# (sequence protocol)

# dict comprehension

{ l : 0 for l in string.ascii_lowercase }

# we could also use c.get(i, 0) to define default value
# or we could use collections.counter which derives from dict with
# a __missing__ method that sets element to 0

class mydict(dict):

   def __missing__(self, x):
       return 0

x = mydict()
x[10]

# find vs index
# on strings, find and index methods are available. Index raises a
# exception if can't find substring. Find returns -1. Better option.
# On lists, only index is available.
# https://stackoverflow.com/questions/9542738/python-find-in-list

l = "i'm working"
assert l.find("not") == -1
assert "working" in l

l = [1, 2, 3, 4, 5]
assert l.index(1) == 0

# better to use "in" if I don't need the index
1 in l

# finding first element that satisifies a condition

g = next(i for (i,x) in enumerate([1,2,3,4]) if x >= 2)
g = next((i for (i,x) in enumerate([1,2,3,4]) if x >= 2), None)

# Useful collections

https://docs.python.org/3/library/collections.html#collections.deque

collection.Counter # like a dict but initially everything is set to 0
collection.deque # like list with constant time left insert (appendleft) and pop

task_counts = collections.Counter(tasks)

# reverse a list
s[::-1]   # slice notation can take a third parameter
s[-1::-1]
''.join(reversed(s))


# Cool python trick
def find_min(l, i):
    return min((l[j], j) for j in range(i, len(l)))[1]

# don't use mutable default variables
def f(y, x = []):
    x.append(y)
    print(x)

# cool trick
a = [6, 3, 1, 2, 5, 4]
sorted(range(len(a)), key=a.__getitem__)
# [2, 3, 1, 5, 4, 0]

# format
print("Case #{}: {} {}".format(i, n + m, n * m))
# use f-string

# count element in matrix
def mat_count(mat, i, ii, j, jj, val):
  return sum( mat[a][b] == val for a in range(i,ii) for b in range(j,jj) )

# binary
>>> bin(42)
'0b101010'
>>> int(bin(42), 2)
42

# count bits of a number

bin(100).count('1')

# del and pop

>>> a = list(range(100))
>>> del a[1:99]
>>> a
[0, 99]
>>> del a[0]
>>> a
[99]
>>> a.pop()
99
>>> a
[]

# Careful with operator precedence

a, b == c, d
# is not the same as   (a, b) == (c, d)