#TAGS array, greedy

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        index = {}
        n = len(S)
        for i, c in enumerate(S):
            index[c] = i

        i = 0
        res = []
        while i < n:
            num = 0
            last_cur_split = i
            while i <= last_cur_split:
                c = S[i]
                last_cur_split = max(last_cur_split, index[c])
                i += 1
                num += 1
            res.append(num)
        return res
        
