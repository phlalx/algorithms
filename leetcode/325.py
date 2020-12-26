#TAGS 2-sum

# class Solution:
#     def maxSubArrayLen(self, nums: List[int], k: int) -> int:
#         acc = [0]
#         for v in nums:
#             acc.append(acc[-1] + v)
#         seen = {0:0}
#         res = 0
#         for i, v in enumerate(acc):
#             j = seen.get(v-k)
#             if j is not None:
#                 res = max(res, i - j)
#             seen.setdefault(v, i)
#         return res

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        cur = 0
        seen = {}
        seen[cur] = -1
        best = 0
        for i, v in enumerate(nums):
            cur += v
            j = seen.get(cur - k)
            if j is not None and i - j > best:
                best = i - j
            seen.setdefault(cur, i)
        return best
