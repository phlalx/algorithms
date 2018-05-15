

g = [ None ] * 3
g[0] = [1]
g[1] = [0,2]
g[2] = [0]

memo = {}

def is_path(i, j):
    res = memo.get((i, j))
    if res is not None:
        return res 
    
    if i == j:
        res = True
    else:
        res = False
        for s in g[i]:
            if is_path(s, j):
                res = True
                break

    memo[(i, j)] = res
    return res

for i in range(3):
    for j in range(3):
        print(i, j, is_path(i, j))
