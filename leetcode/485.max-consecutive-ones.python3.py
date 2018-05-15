# TAGS array

# 
# class Solution:
#     def findMaxConsecutiveOnes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         best_streak = 0
#         cur_streak = 0
#         for i in nums:
#             if i == 1:
#                 cur_streak += 1
#                 best_streak = max(best_streak, cur_streak)
#             else:
#                 cur_streak = 0
#         return best_streak

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        i = 0
        n = len(nums)
        best = 0
        while i < n:
            seq = 0
            while i < n and nums[i] == 1:
                seq += 1
                best = max(best, seq)
                i += 1
            while i < n and nums[i] == 0:
                i += 1
        return best

