#TAGS easy but corner case

# Solution 1 with sorting
class Solution:
    def findErrorNums(self, nums):
        nums.sort()
        b = None
        for cur, nex in zip(nums, nums[1:]):
            if cur == nex:
                a = cur
            if cur + 2 == nex:
                b = cur + 1
        if b is None:
            b = 1 if nums[0] != 1 else nums[-1] + 1
        return a, b

# Solution 2 linear time constant space
class Solution:
    def findErrorNums(self, nums):
        nums = [ v - 1 for v in nums ]  # translate to 0..n-1
        n = len(nums)
        i = 0
        dup, i_dup = None, None
        while i < n:
            if nums[i] == i:
                # fine, right place already
                i += 1
            else:
                # give names and make diagram to avoid confusion
                #  --------- i ------- a -------
                # nums       a         b
                a = nums[i]
                b = nums[a]
                if a == b:
                    # it means b is the duplicate, and it is at its place
                    # we can't get nums[i] right
                    dup = a
                    i_dup = i
                    i += 1
                else:
                    nums[i], nums[a] = b, a
                    # we just moved a to its right place
                    # did we move the duplicate element? if so, update its index
                    if b == dup:
                        i_dup = i
        return (dup+1), (i_dup+1)
