# KMP

# key-structure table of prefix
# let be a string s
#   beta: i -> longest proper self-prefix of s   PSP, bord en français
#   beta: 0 -> 0
#
# key ideas
# - PSP relation is transitive u < v < w => u < w
# - si u < w and v < w then u < v, u = w, or v < u
#  => To find all the PSP of a word, iterate over beta
# - table of prefixes can be defined recursively.
#      If v.x a PSP of u.x, then v is a PSP of u.
#      We can then find all PSPs by iterating over beta(u)
#

# TODO why proper
#  implement KMP without concatenation
#  why is this linear time?

def prefixes(u):
    n = len(u)
    res = [ None ] * n  # prefix table, res[i] = len of PSP for u[:i+1]
    res[0] = 0
    for i in range(1, n):
        x = u[i]
        # we find the longest PSP of u[:i] followed by x
        k = i - 1
        while k >= 0 and u[res[k]] != x:
            k = res[k] - 1
        res[i] = 0 if k < 0 else res[k] + 1
    return res

u = "abaaba"
expected = [0, 0, 1, 1, 2, 3]
actual = prefixes(u)

# substring search reduction to PSP find

print(u, expected, actual, sep = '\n')

s = 'haystackneedlehaystackneedle'
t = 'needle'

pre = prefixes(t + '#' + s)
for i, l in enumerate(pre):
    if l == len(t):
        print(i - 2 * len(t))
