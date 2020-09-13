# Games

2 player games. Each player plays optimally. Who wins?

```
def f(state, player):
    if player:
        best = float('-inf')
        for move, new_state in moves(state, player):
            best = max(score(move) + f(new_state, not player)
        return best
    else:
        best = float('inf')
        for move, new_state in moves(state, player):
            best = min(score(move) + f(new_state, not player)
        return best
```

If there is symetry in the problem

```
def f(state, player):
    best = float('-inf')
    for move, new_state in moves(state, player):
        best = max(score(move) - f(new_state, not player)
    return best
```
