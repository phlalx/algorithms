# TAGS string
# TODO execution time isn't good enough.. 40%. I tried different implementations
# of this idea without success. Maybe a different algorithm can do better...
class Solution:
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        if len(s) < 2:
            return []
        for i in range(len(s) - 1):
            if s[i : i + 2] == "++":
                # replace part of a string
                res.append("".join([s[:i], "--", s[i + 2 :]]))
        return res
