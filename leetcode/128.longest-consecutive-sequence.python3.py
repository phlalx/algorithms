# TAGS array dfs cool
# Note: recursive DFS fail test, recursion limit exceeded


def diam(s, i, seen):
    right = i
    left = i
    seen.add(i)
    while right + 1 in s:
        right += 1
        seen.add(right)
    while left - 1 in s:
        left -= 1
        seen.add(left)
    return right - left + 1


class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        seen = set()
        res = max((diam(s, i, seen) for i in s if not i in seen), default=0)
        return res
