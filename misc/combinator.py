
# Example of dynamic programming with space optimization
# Because we only need the previous line in the dependency relation,
# we only need to store two lines, the previous line, and the one being
# computed

def c(n, p):
    memo = [[ 1 ] * (p+1) for _ in range(2)]
    for i in range(1, n+1):
        for j in range(1, min(i, p+1)):
            memo[i % 2][j] = memo[(i-1) % 2][j] + memo[(i-1) % 2][j-1]
    return memo[n % 2][p]

for i in range(10):
    print([c(i, j) for j in range(i+1)])
