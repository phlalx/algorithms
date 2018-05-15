# Generation

Generate a set of objects that satisfies a property.

Two classes of solutions
1. backtracking (more general), see [backtracking](./backtracking.md)
2. build the solution incrementally (possible if there is recurence relation)

## Example: generating well-formed parenthesis using Catalan relation (!22)

```
def generateParenthesis(n):
    res = [ None ] * (n+1)
    res[0] = ['']
    res[1] = [ '()' ]
    for i in range(2, n+1):
        s = []
        for j in range(i):
            for exp1 in res[j]:
                for exp2 in res[i - 1 - j]:
                    s.append( '(' +  exp1 + ')' + exp2)
        res[i] = s
    return res[n]
```