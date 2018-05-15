# TAGS string


class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res = []
        N = S.count("-")
        num_char = len(S) - N
        rem = num_char % K
        if rem == 0:
            rem = K
        group_size = rem
        for c in S:
            if c == "-":
                continue
            if group_size == 0:
                res.append("-")
                group_size = K
            res.append(c.upper())
            group_size -= 1
        return "".join(res)
