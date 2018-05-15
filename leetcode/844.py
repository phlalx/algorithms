#TAGS string, double pointer
# TODO constant space

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def reduce(S):
            st = []
            for c in S:
                if c == '#':
                    if st:
                        st.pop()
                else:
                    st.append(c)
            return st
        return reduce(S) == reduce(T)


