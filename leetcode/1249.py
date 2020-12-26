#TAGS parenthesis, greedy

# I got the right idea but because it didn't feel "right", I tried
# backtracking which worked but was TLE
#

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        remove = set()
        n = len(s)
        for i, p in enumerate(s):
            if p == '(':
                st.append(i)
            elif p == ')':
                if st:
                    st.pop()
                else:
                    remove.add(i)
        remove.update(st)  # pythonic
        res = [s[i] for i in range(n) if i not in remove]
        return ''.join(res)


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        opened = 0
        for c in s:
            if c == ')':
                if opened > 0:
                    res.append(c)
                    opened -= 1
            elif c == '(':
                opened += 1
                res.append(c)
            else:
                res.append(c)
        real_res = []
        for c in reversed(res):
            if opened > 0 and c == '(':
                opened -= 1
            else:
                real_res.append(c)
        return (''.join(real_res))[::-1]