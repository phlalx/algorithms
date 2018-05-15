# TAGS brute force

letter_per_digit = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


def f(digits, i, cur, res):
    if i == len(digits):
        res.append("".join(cur))
    else:
        for c in letter_per_digit[int(digits[i])]:
            cur.append(c)
            f(digits, i + 1, cur, res)
            cur.pop()


def iter(digits):
    res = [""]
    for digit in digits:
        cur_res = res
        res = []
        d = int(digit)
        for c in letter_per_digit[d]:
            for s in cur_res:
                res.append(s + c)
    return res


from itertools import product


def pythonic(digits):
    res = []
    t = tuple(letter_per_digit[int(d)] for d in digits)
    return ["".join(u) for u in product(*t)]


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits in ["", "0", "1"]:
            return []
        return pythonic(digits)
