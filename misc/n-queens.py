import itertools

def solve(N):

    pos = [ None ] * N

    def aligned(x, y, a, b):
        if y == b:
            return True
        if x - y == a - b:
            return True
        if x + y == a + b:
            return True
        return False

    def check(i):
        for k in range(i):
            if aligned(k, pos[k], i, pos[i]):
                return False
        return True

    def f(i):
        if i == N:
            print(pos)
            return True
        for j in range(N):
            pos[i] = j
            if check(i) and f(i+1): 
                return True
        return False

    return f(0)

print(solve(6))