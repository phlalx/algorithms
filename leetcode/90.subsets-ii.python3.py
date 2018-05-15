# TAGS recursive


def subsets(nums):
    if not nums:
        return {()}
    a = nums[0]
    nums.remove(a)
    ss = subsets(nums)
    res = ss.copy()
    for i in ss:
        candidate_set = (a,) + i
        res.add(candidate_set)
    return res


class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = subsets(nums)
        return list(map(list, res))


def test():
    i = [1, 2, 2]
    r = Solution().subsetsWithDup(i)
    print(r)


if __name__ == "__main__":
    test()
