# TAGS dfs
# read the question well: it's the number of longest increasing subsequence
# not the the longest of increasing subsequence
# memoize two info: longest sequence, number of such sequence


class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # lis[i] contains the longest sequence length ending at i,  and the
        # number of such sequences
        lis = [None] * len(nums)
        lis_len = 0
        for i in range(len(nums)):
            cur_max = 0
            cur_num = 0
            for j in range(i):  # can we rewrite this more cleanly?
                if nums[j] >= nums[i]:
                    continue
                max_seq_len, num_of_seq = lis[j]
                max_seq_len += 1
                if max_seq_len == cur_max:
                    cur_num += num_of_seq
                elif max_seq_len > cur_max:
                    cur_max = max_seq_len
                    cur_num = num_of_seq
            if cur_max == 0:
                cur_max = 1
                cur_num = 1
            lis[i] = cur_max, cur_num
            lis_len = max(lis_len, cur_max)
        print(lis)
        return sum(num for (llis, num) in lis if llis == lis_len)


def test():
    # l = [1,3,5,4,7]
    l = [2, 2, 2, 2, 2]
    print(Solution().findNumberOfLIS(l))


test()
