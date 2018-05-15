#TAGS parenthesis, greedy
#TODO constant space

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
