def f(s):
    a = False
    late = 0
    for c in s:
        if c == "A":
            if a:
                return False
            else:
                a = True
            late = 0
        elif c == "L":
            late += 1
            if late == 3:
                return False
        else:
            late = 0
    return True


class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return f(s)
