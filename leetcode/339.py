#TAGS tree
# trivial

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nested, level):
            if nested.isInteger():
                return level * nested.getInteger()
            l = nested.getList()
            res = sum(dfs(v, level+1) for v in l)
            return res
        return sum(dfs(v, 1) for v in nestedList)
            
