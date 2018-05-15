# TAGS array, cool
# simple but tricky, need to think of the right invariant

# crux: if b > c, we can of course increase c, but BETTER to decrease b if
# possible, so we need to consider a sliding window of 3 elements.
#
# we first think of the general case, sliding window with a <= b,
# and then we deal with initial cases


def non_decreasing(nums):
    n = len(nums)

    if n <= 2:
        return True

    joker = True

    if n >= 3 and nums[0] > nums[1]:
        joker = False
        nums[0] = nums[1]

    assert n >= 3
    for i in range(n - 2):
        a = nums[i]
        b = nums[i + 1]
        c = nums[i + 2]
        assert a <= b  # important invariant! trick
        if b <= c:
            continue
        if not joker:
            return False
        joker = False
        # b and c aren't ordered properly
        # we greedily favor decreasing b if we can
        # otherwise we increase c
        if a <= c:
            nums[i + 1] = a
        else:
            nums[i + 2] = b
    return True


class Solution:
    def checkPossibility(self, nums):
        return non_decreasing(nums)
