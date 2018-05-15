
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

class Matcher:

    def __init__(self, pattern):
        self.pattern = pattern
        self.prefixes = prefixes(pattern)
        self.cur = 0 # next to match

    def feed(self, char) -> bool:
        i = self.cur
        while i >= 1 and self.pattern[i] != char:
            i = self.prefixes[i-1]
        if self.pattern[i] == char:
            i += 1
        if i == len(self.prefixes):
            self.cur = 0
            return True
        else:
            self.cur = i
            return False

matcher = Matcher("ok google")

string = "bla bla ok gook google bla ok google "

for c in string:
    res = matcher.feed(c)
    print(res)
