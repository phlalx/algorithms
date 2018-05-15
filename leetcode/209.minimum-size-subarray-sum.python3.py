# TAGS array, sliding window, binary search, cool
# https://leetcode.com/problems/minimum-size-subarray-sum/discuss/59093/Python-O(n)-and-O(n-log-n)-solution
# See 862 for a generalization to all numbers

from bisect import bisect_right

# return biggest index in [i, j) such that tab[index] <= x
# def f(tab, x, i, j):
#     return max((k for k, v in enumerate(tab[i:j]) if v <= x), default=None)


def f(tab, x, i, j):
    k = bisect_right(tab, x, i, j)
    return k - 1 if k else None


assert f([1, 3, 6, 8], 3, 0, 2) == 1


def partial_sum(nums, k):
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]
    # prefix[b] - prefix[a] = sum(nums[a:b])
    best = float("inf")
    for j in range(1, n + 1):
        # we look up the biggest i such that sum(i, j) >= k
        # <=> prefix[i] <= prefix[j] - k
        i = f(prefix, prefix[j] - k, 0, j)
        if i is not None:
            best = min(best, j - i)
    return best if best != float("inf") else 0


def sliding_window(nums, s):
    cur_sum = 0
    best = float("inf")
    i = 0
    for j, v in enumerate(nums):
        cur_sum += v
        if cur_sum < s:
            continue
        while i <= j and cur_sum >= s:
            best = min(j - i + 1, best)
            cur_sum -= nums[i]
            i += 1
    return best if best != float("inf") else 0


class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        return partial_sum(nums, s)
