# TAGS loop invariant, big int, cool


class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        n -= 1

        # We are looking for digit n (0-based), starting from start
        # nbr_of_digits is the number_of_digits of start

        start = 1
        nums_with_nbr_digit = 9
        nbr_of_digits = 1
        while n >= nums_with_nbr_digit * nbr_of_digits:
            n -= nums_with_nbr_digit * nbr_of_digits
            start += nums_with_nbr_digit
            nbr_of_digits += 1
            nums_with_nbr_digit *= 10

        q, n = divmod(n, nbr_of_digits)
        start += q

        return int(str(start)[n])
