# TAGS lexer, tricky, ad-hoc
# Trick is to write the right lexer
# choose simple form for tokens ("+234x", "=")
# then add coefficient and constant


def get_monome(s):
    chars = iter(s)
    c = next(chars, None)
    while c:
        # c is the first non-read
        if c == "=":
            yield "="
            c = next(chars, None)
        elif c == "x":
            yield "x"
            c = next(chars, None)
        else:
            # we could reuse the same buffer for efficiency
            buf = [c]
            c = next(chars, None)
            while c is not None and c not in {"=", "+", "-"}:
                buf.append(c)
                c = next(chars, None)
            assert buf
            yield "".join(buf)


class Solution:
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        total_coef = 0
        total_const = 0

        reverse = 1
        for s in get_monome(equation):
            if s == "=":
                reverse = -1
            elif s[-1] == "x":  # monome
                c = s[:-1]
                if c in {"+", "-", ""}:
                    c = c + "1"
                total_coef += reverse * int(c)
            else:  # constant
                total_const += reverse * int(s)

        if total_coef == 0:
            if total_const == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return "x=" + str(-total_const // total_coef)
