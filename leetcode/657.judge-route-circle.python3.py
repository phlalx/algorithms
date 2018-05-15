class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        u, l = 0, 0
        for m in moves:
            if m == "U":
                u += 1
            elif m == "D":
                u -= 1
            elif m == "L":
                l += 1
            else:
                l -= 1
        return not u and not l
