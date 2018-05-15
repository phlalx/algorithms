# TAGS new
# greedy + recursive/stack, see 321, 503, 1081
#
# We can find the leftmost letter of the solution greedily
#
# Note to myself, don't give up too soon on finding a greedy solution

# Unoptimized solution, without datastructure
#
def ok(s, i, remain):
    return all(x in s[i:] for x in remain)

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        res = []
        cur = 0
        remain = set(s)
        num_unique = len(remain)
        for k in range(num_unique):
            v,  i = min((s[i], i) for i in range(cur, n) if ok(s, i, remain) and s[i] not in res)
            res.append(v)
            cur = i + 1
            remain.discard(v)
        return "".join(res)


# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         assert 0


# s = Solution().removeDuplicateLetters("cbacdcbc")
# print(s)
