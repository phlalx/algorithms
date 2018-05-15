# TAGS lexer, generator


def tokenize(line):
    n = len(line)
    i = 0

    while i < n:
        c = line[i]
        if c.isdigit():
            res = []
            while i < n and line[i].isdigit():
                res.append(line[i])
                i += 1
            yield "".join(res)
        else:
            i += 1
            yield c

    # Don't raise StopIteration in generator


# class tokenize:

#     def __init__(self, line):
#         self.line = line
#         self.i = 0
#         self.n = len(line)

#     def __next__(self):
#         if self.i == self.n:
#             raise StopIteration
#         c = self.line[self.i]
#         if c.isdigit():
#             res = []
#             while self.i < self.n and self.line[self.i].isdigit():
#                 res.append(self.line[self.i])
#                 self.i += 1
#             return "".join(res)
#         else:
#             self.i += 1
#             return c

#     def __iter__(self):
#         return self


def test():
    tokens = tokenize("abc12a4")
    l = list(tokens)
    assert l == ["a", "b", "c", "12", "a", "4"]


class Solution:
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i = 0
        n = len(word)
        tokens = tokenize(abbr)
        for tok in tokens:
            if tok.isdigit():
                if tok[0] == "0":
                    return False
                i += int(tok)
            elif i >= n or tok != word[i]:
                return False
            elif tok.isdigit():
                i += int(tok)
            else:
                i += 1
        return i == n
