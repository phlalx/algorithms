#TAGS backtrack
# easy

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        cur = []
        n = len(nums)
        res = []
        def dfs(i):
            if i == n:
                res.append(list(cur)) # don't rememmber to copy cur
                return
            for v in nums:
                if v in cur:
                    continue
                cur.append(v)
                dfs(i+1)
                cur.pop()
        dfs(0)
        return res
