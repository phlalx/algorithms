# TAGS string


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            a, b = b, a

        b = b.rjust(len(a), "0")

        carry = 0
        res = []
        for i in reversed(range(len(a))):
            sum_digit = int(a[i]) + int(b[i]) + carry
            assert sum_digit <= 3
            if sum_digit == 3:
                digit = "1"
                carry = 1
            elif sum_digit == 2:
                digit = "0"
                carry = 1
            else:
                digit = str(sum_digit)
                carry = 0
            res.append(digit)
        if carry:
            res.append("1")
        return "".join(reversed(res))


# Better solution
from itertools import zip_longest

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        cr = 0
        res = []
        for b1, b2 in zip_longest(reversed(a), reversed(b), fillvalue='0'):
            b1 = int(b1)
            b2 = int(b2)
            x = int(b1) + int(b2) + cr
            cr = x // 2
            res.append(str(x % 2))
        if cr:
            res.append(str(cr))
        return ''.join(reversed(res))



