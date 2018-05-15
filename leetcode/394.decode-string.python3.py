# TAGS parser
# see 726, 227
#
# TODO general solution but there must be a simpler solution
#
# This is a parsing problem.
# Start to writer a lexer using a generator
#

# E := A*
# A := str | num [ E ]

# Solution 1
# Lexer + synthetise result
#
# Verbose, lot of appends

class Tokenizer:
    def __init__(self, s):
        self.s = s
        self.i = 0
        self.n = len(s)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == self.n:
            raise StopIteration
        c = self.s[self.i]
        if c == "[" or c == "]":
            self.i += 1
            res = c
        elif c.isdigit():
            count = int(c)
            self.i += 1
            while self.i < self.n and self.s[self.i].isdigit():
                count = count * 10 + int(self.s[self.i])
                self.i += 1
            res = str(count)
        else:
            res = [c]
            self.i += 1
            while self.i < self.n and self.s[self.i].isalpha():
                res.append(self.s[self.i])
                self.i += 1
            res = "".join(res)
        return res

def best_tokenizer(s):
    # easier to use a generator
    it = iter(s)
    c = next(it)
    while c is not None:
        if c == '[' or c == ']':
            yield c
            c = next(it, None)
        elif c.isdigit():
            res = 0
            while c is not None and c.isdigit():
                res = 10 * res + int(c)
                c = next(it, None)
            yield str(res)
        else:
            res = []
            while c is not None and c.isalpha():
                res.append(c)
                c = next(it, None)
            yield ''.join(res)

def parse(tokenizer):

    cur = next(tokenizer, None)  # use nonlocal, less overheader than class

    def parse_A():
        nonlocal cur
        assert cur is not None
        res = ""
        if cur.isdecimal():
            count = int(cur)
            assert "[" == next(tokenizer, None)
            cur = next(tokenizer)
            x = parse_E()
            assert "]" == cur
            res = count * x
            cur = next(tokenizer, None)
        else:
            res = cur
            cur = next(tokenizer, None)
        return res

    def parse_E():
        res = ""
        while not (cur is None or cur == "]"):
            res += parse_A()
        return res

    return parse_E()

class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        tokenizer = best_tokenizer(s)
        return parse(tokenizer)

## Second solution, solution is built by append only
## parse returns the index on the str where it started to copy its result 

def parse(tokenizer, res):

    cur = next(tokenizer, None)  # use nonlocal, less overheader than class

    def parse_A(res):
        nonlocal cur
        assert cur is not None
        i = None
        if cur.isdecimal():
            count = int(cur)
            assert "[" == next(tokenizer, None)
            cur = next(tokenizer)
            i = parse_E(res)
            j = len(res)
            assert "]" == cur
            for _ in range(count-1):
                res.extend(res[i:j])
            cur = next(tokenizer, None)
        else:
            i = len(res)
            res.extend(cur)
            cur = next(tokenizer, None)
        return i

    def parse_E(res):
        i = len(res)
        while not (cur is None or cur == "]"):
            parse_A(res)
        return i

    return parse_E(res)

class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        tokenizer = best_tokenizer(s)
        res = []
        parse(tokenizer, res)
        return ''.join(res)


def test():
    print(Solution().decodeString('3[a2[c]]'))

# test()


class Solution:
    def decodeString(self, s):
        st = []
        cur_num = 0
        res = []
        for c in s:
            if c.isdigit():
                cur_num = 10 * cur_num + int(c)
            elif c == '[':
                st.append( (cur_num, len(res)))
                cur_num = 0
            elif c == ']':
                rep, pos = st.pop()
                res.extend(res[pos:] * (rep - 1))
            else:
                res.append(c)

        return ''.join(res)