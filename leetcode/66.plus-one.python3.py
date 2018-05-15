# TAGS string, bigint


class Solution:
    def plusOne(self, s):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        res = []
        for d in reversed(s):
            x = int(d) + carry
            if x >= 10:
                x -= 10
                carry = 1
            else:
                carry = 0
            res.append(x)
        if carry:
            res.append(1)
        return res[::-1]
