def powrec(x, n):
    if n == 1:
        return x
    elif n % 2 == 0:
        return powrec(x * x, n // 2)
    else:
        return x * powrec(x * x, n // 2)


def powiter(x, n):
    res = x
    u = 1.0
    # n0 = n
    while n >= 2:
        # invariant u * res ^ n = x ^ n0
        if n % 2 == 0:
            res = res * res
            n = n // 2
        else:
            u = res * u
            n = n - 1
    return u * res


class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        if x == 0.0:
            return 0.0
        if n < 0:
            x = 1.0 / x
            n = (
                -n
            )  # careful if n = MIN_INT, does not matter in python, but use long int in C++
        return powiter(x, n)
