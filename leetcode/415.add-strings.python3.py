# TAGS string, bigint


class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n = max(len(num1), len(num2))
        num1 = num1.zfill(n)
        num2 = num2.zfill(n)
        carry = 0
        res = []
        for u, v in zip(reversed(num1), reversed(num2)):
            x = int(u) + int(v) + carry
            res.append(str(x % 10))
            carry = x // 10
        if carry:
            res.append("1")
        return "".join(reversed(res))
