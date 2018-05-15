# TAGS bigint
# TODO do without reverse operations

BASE = 10


def multiply(a, b):
    p = len(a)
    q = len(b)
    prod = [0] * (p + q)
    for a_i in range(p):
        carry = 0
        for b_i in range(q):
            prod[a_i + b_i] += carry + a[a_i] * b[b_i]
            carry = prod[a_i + b_i] // BASE
            prod[a_i + b_i] = prod[a_i + b_i] % BASE
        prod[a_i + q] += carry
    return prod


class Solution:
    def multiply(self, a, b):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a = [int(d) for d in reversed(a)]
        b = [int(d) for d in reversed(b)]
        prod = multiply(a, b)
        res = "".join(str(d) for d in reversed(prod)).lstrip(
            "0"
        )  # TODO do without lstrip
        return res if res else "0"
