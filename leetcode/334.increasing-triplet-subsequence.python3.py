# TAGS array, cool, greedy
# trick: keep strictly increasing min (for that, we need to keep the cur min too)


# General solution: longest increasing subsequence
#
# import functools
#
# class Solution:
#     def increasingTriplet(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         @functools.lru_cache(maxsize=None)
#         def lcis(i):
#           return max( (lcis(j) + 1 for j in range(i) if nums[j] < nums[i]), default = 1 )

#         if not nums:
#             return False
#         res = max(lcis(i) for i, _ in enumerate(nums))
#         # print(res)
#         return res >= 3

# Maintains two min, the current min, and the current strictly
# increasing min. Actually very simple.
class Solution:
    def increasingTriplet(self, nums):
        cur_min = float("inf")
        cur_increasing_min = float("inf")
        for v in nums:
            if v <= cur_min:
                cur_min = v
            elif v <= cur_increasing_min:
                cur_increasing_min = v
            else:
                return True
        return False
