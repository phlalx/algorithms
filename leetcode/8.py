class Solution:
    def myAtoi(self, str: str) -> int:
        res = 0
        i = 0
        n = len(str)
        while i < n and str[i] == ' ':
            i += 1
        if i == n:
            return 0
        sign = 1
        if str[i] == '+':
            i += 1
        elif str[i] == '-':
            sign = -1
            i += 1
        elif not str[i].isdigit():
            return 0
        while i < n and str[i].isdigit():
            res = 10 * res + int(str[i])
            i += 1
        if not (-(2 ** 31) <= res <= 2 ** 31 - 1):
            if sign == 1:
                return 2 ** 31 - 1
            else:
                return -(2 ** 31)
        return res * sign
        
