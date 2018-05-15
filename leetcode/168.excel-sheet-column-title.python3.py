class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        assert n >= 1
        res = ""
        while True:
            rem = (n - 1) % 26 + 1
            res = chr(ord("A") + rem - 1) + res
            n = (n - rem) // 26
            if not n:
                break
        return res
