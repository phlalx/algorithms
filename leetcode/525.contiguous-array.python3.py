# TAGS array
# similar to the target-sum problem and 325


class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {0: 0}
        res = 0
        alt = 0
        for i, v in enumerate(nums):
            alt += 1 if v else -1
            j = seen.get(alt)
            if j is not None:
                res = max(res, i + 1 - j)
            else:
                seen[alt] = i + 1
        return res
