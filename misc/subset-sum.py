# TAGS dp
# classic dp problem  https://en.wikipedia.org/wiki/Subset_sum_problem

import functools

# Recusive version

def sum(l):

    @functools.lru_cache(maxsize=None)
    def sum_aux(i, S):
        if i == len(l) - 1:
            res = S == l[i]
        else:
            res = sum_aux(i+1, S) or sum_aux(i+1, S - l[i])
        return res

    return sum_aux(0, 0)

# Recursive version with solution, method 1

def sum2(l):

    memo = {}

    def sum_aux(i, S):
        res = memo.get( (i, S),  None)
        if res:
            return res

        if i == len(l) - 1:
            res = S == l[i]
        else:
            res = sum_aux(i+1, S) or sum_aux(i+1, S - l[i])
        memo[(i, S)] = res
        return res

    def print_sol(i, S):

        if i == len(l) - 1:
            assert S == l[i]
            print(i)
        else:
            if memo[(i+1, S)]:
                print_sol(i+1, S)
            elif memo[(i+1, S - l[i])]:
                print(i)
                print_sol(i+1, S - l[i])

    sum_aux(0, 0)
    if memo[0,0]:
        print_sol(0, 0)

    return memo[0,0]


# Recursive version with solution
# Unnecessary appends

def sum_sol(l):

    # there is a subsequence s of l[i:] such that sum(s) == S
    @functools.lru_cache(maxsize=None)
    def sum_aux(i, S):
        if i == len(l) - 1:
            is_sol = S == l[i]
            res = is_sol, [i] if is_sol else None
        else:
            res1, u = sum_aux(i+1, S)
            res2, v = sum_aux(i+1, S - l[i])
            if res1:
                res = res1, u
            elif res2:
                res = res2, [i] + v
            else:
                res = False, None
        return res

    return sum_aux(0, 0)


def main():
    tests = [[1], [-1, 1], [-100,10,-9,4,-1], [1,2,3,4], [-2,-4]]
    for t in tests:
        print(t, sum2(t))

main()






