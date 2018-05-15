#TAGS stack
#easy

 class Solution:
    def removeDuplicates(self, S: str) -> str:
        st = ['$']
        for c in S:
            if c == st[-1]:
                st.pop()
            else:
                st.append(c)
        return ''.join(st[1:])
