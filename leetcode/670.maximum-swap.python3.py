# TAGS recursive, cool
#
# Similar to stock price exercise
# scan array from right to left
# remember cur_max seen so far
# if nums[i] is small than cur_max, update swap candidate


def g(digits):
    i = j = i_max = len(digits) - 1
    cur_max = digits[-1]
    for k in reversed(range(len(digits) - 1)):
        d = digits[k]
        if d > cur_max:
            cur_max = d
            i_max = k
        elif d == cur_max:
            pass
        else:
            i = i_max
            j = k
    return i, j


def f(s, k):
    if k == len(s) - 1:
        return k, k, k
    i_max, i, j = f(s, k + 1)
    if s[k] < s[i_max]:
        return i_max, k, i_max
    elif s[k] == s[i_max]:
        return i_max, i, j
    else:
        return k, i, j


class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num:
            return 0
        s = list(str(num))  # pythonic
        #        _, i, j = f(s, 0)
        i, j = g(s)
        s[i], s[j] = s[j], s[i]
        return int("".join(s))
