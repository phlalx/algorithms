# TAGS array, cool
# see also 128


class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        res = []
        nums.append(None)  # sentinel
        it = iter(nums)
        bgn = end = next(it)
        for elt in it:
            if elt == end + 1:
                end += 1
            else:
                res_str = str(bgn) if bgn == end else "{}->{}".format(bgn, end)
                res.append(res_str)
                bgn = end = elt
        return res
