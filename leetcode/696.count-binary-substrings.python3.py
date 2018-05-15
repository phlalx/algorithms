def f(nums):
    counts = []
    cur = nums[0]
    cur_count = 1
    for num in nums[1:]:
        if num != cur:
            counts.append(cur_count)
            cur_count = 1
            cur = num
        else:
            cur_count += 1
    counts.append(cur_count)
    res = 0
    for i in range(len(counts) - 1):
        res += min(counts[i], counts[i + 1])
    return res


class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        return f(s)
