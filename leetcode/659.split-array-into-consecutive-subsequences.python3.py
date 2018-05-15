# TAGS greedy, cool
# found it very tricky
# TODO we may not need sorting
# REDO
# See 128, 856 simpler versions, 
# It would be easy without duplicate

# Once we settle on a greedy strategy, it becomes rather straightforward
# We know that each elements is either the start of a new sequence
# or it should be append to a new sequence
#
# We greedily append to the shortest existing sequence
#
# Also note that we only need to remember the most recent end of all sequence
#
# It's ad-hoc but a cool greedy problem

from collections import Counter


class Solution:
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        c = sorted(Counter(nums).items())
        # for each number, we know their count

        cur = -40
        num_one = 0
        num_two = 0
        num_three = 0

        for v, n in c:
            assert num_one >= 0
            assert num_two >= 0
            assert num_three >= 0
            if v == cur + 1:  # element extend cur sequence
                if n < num_one:
                    return False
                n -= num_one
                if n < num_two:
                    return False
                n -= num_two
                if n > num_three:
                    new_num_one = n - num_three
                else:
                    new_num_one = 0
                    num_three = n
                num_three += num_two
                num_two = num_one
                num_one = new_num_one
            elif num_two + num_one > 0:
                return False
            else:
                num_one = n
            cur = v
        return num_one == 0 and num_two == 0
