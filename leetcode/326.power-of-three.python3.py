# TAGS trick


class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (
            n > 0 and 3 ** 20 % n == 0
        )  # we suppose we know the biggest possible power

        # def ispowerof3(n)
        #   if n < 1:
        #       return False
        #   while n % 3 == 0:  # divide n by 3 as many times as possible
        #       n //= 3
        #   return True if n == 1 else False

        #   def ispowerof3(n):
        #   # find the smallest power of 3 just above n
        #     if n < 1:
        #       return False
        #     u = 1
        #     while u < n:
        #       u *= 3
        #     return n == u
