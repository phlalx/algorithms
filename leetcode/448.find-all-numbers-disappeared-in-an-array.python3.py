def fast(nums):
    n = len(nums)
    c = [False] * n
    for v in nums:
        c[v - 1] = True
    res = []
    for i, b in enumerate(c):
        if not b:
            res.append(i + 1)
    return res


def constantspace(v):
    n = len(v)
    for i in range(n):  # easier to reason with values in range(n)
        v[i] = v[i] - 1
    i = 0
    while i < n:
        cur = v[i]
        if cur is None:
            i += 1
        elif cur == i:  # i is correctly-filled
            i += 1
        elif v[cur] == cur:  # the place where cur should be is already correctly-filled
            v[i] = None
            i += 1
        else:
            v[cur], v[i] = cur, v[cur]
    res = [i + 1 for i, e in enumerate(v) if e is None]
    return res


# print(constantspace([3,1,2]))


class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return constantspace(nums)
