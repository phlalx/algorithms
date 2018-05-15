# TAGS array, cool, pythonic
# See also 26, 238

# TAGS array
# TODO not in constant memory space
#
# class Solution:
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         d = dict()
#         res = []
#         for i in nums:
#             if i in d:
#                 d[i] = min(2, d[i] + 1)
#             else:
#                 d[i] = 1
#         for k, v in d.items():
#             res.extend([k] * v)
#         res.sort()
#         nums[0:] = res[0:]
#         return len(res)
#
# # sol = Solution()
# # res = sol.removeDuplicates([1,1,1,2])
# # print(res)
#

# pythonic
#
# def it(a):
#     dup = False
#     last = None
#     for v in a:
#         if v != last:
#             yield v
#             dup = False
#         elif not dup and v == last:
#             yield v
#             dup = True
#         else:
#             continue
#         last = v
#
# class Solution:
#     def removeDuplicates(self, nums):
#         i = 0
#         for v in it(nums):
#             nums[i] = v
#             i += 1
#         return i
#


class Solution:
    def removeDuplicates(self, a):
        n = len(a)
        i = 0
        j = 0
        dup = False
        while j < n:
            a[i] = a[j]
            i += 1
            v = a[j]
            j += 1
            if j == n:
                break
            elif a[j] == v and not dup:
                dup = True
            elif a[j] != v:
                dup = False
            else:
                while j < n and a[j] == v:
                    j += 1
                dup = False
        return i
