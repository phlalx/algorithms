# TAGS string


def f(s):
    cur = s[0]
    rep = 1
    res = []
    for c in s[1:] + "*":
        if c == cur:
            rep += 1
        else:
            res += str(rep) + cur
            cur = c
            rep = 1
    return "".join(res)


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        u = "1"
        for _ in range(n - 1):
            u = f(u)
        return u


def main():
    for i in range(6):
        res = Solution().countAndSay(i)
        print(res)


if __name__ == "__main__":
    main()
