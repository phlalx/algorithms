#TAGS dp

# Not as hard as it seems
# Trick: use skyline as state
# then just implementation, quite simple thanks to pythonic construct
#  (I should try to use slices and index more often)
#
# At the limit of TLE

import functools

class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        @functools.lru_cache(None)
        def f(state):
            if min(state) == m:
                return 0
            height = min(state)
            i = state.index(height)  # pythonic
            res = float('inf')
            state = list(state)
            for j in range(i, n):
                side = j - i + 1
                if state[j] != height or (height + side > m):
                    break
                state[i:j+1] = [height + side] * side
                res = min(f(tuple(state)), res)
            return res + 1
        if m < n:
            m, n = n, m
        init = (0,) * n  # pythonic
        return f(init)
        
