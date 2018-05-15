# TAGS circular array, monotonic stack
# TRICK use a stack, duplicate array
# stack is useful to compute consecutive maxima in an array
# O(n)


class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        n = len(nums)
        res = [None] * n

        stack = list(reversed(nums))
        for i, v in reversed(list(enumerate(nums))):
            while stack and stack[-1] <= v:
                stack.pop()
            res[i] = stack[-1] if stack else -1
            stack.append(v)
        return res
