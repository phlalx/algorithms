# ITERTOOLS

from itertools import permutations, count, combinations

l = 'foobar'

for i, p in zip(count(1), permutations(l)): # all permutations
    print( i, "".join(p) )

for i, p in zip(count(1), permutations(l, 2)): # permutations of all 2-elts subsets (A(n, p))
    print( i, "".join(p) )

for i,  p in zip(count(1), combinations(l, 3)):
    print( i, "".join(p) )

# tentative d'ecrire un generateur pour combinations, 
# marche pas avec une fonction recursive

def comb(l, p):
    cur = []
    n = len(l)

    def f(i, p): # fill cur with p ordered elements in [i:n]
        if p == 0: 
            print(cur)
        for j in range(i, n):
            cur.append(l[j])
            f(j + 1, p - 1)
            cur.pop()
        
    return f(0, p)

comb(l, 3)



    




