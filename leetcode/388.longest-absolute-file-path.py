#TAGS stack, lexer
# easy when it's done but quite hard to get right
# 1. Be careful with corner cases, only count files,
# 2. think of what the lexer returns
# 3. think of using a stack (don't try to write a parser)
# 4. write main loop before bothering with lexer
#       keep current prefix for each line
#
# TODO use prefix sum

import itertools

def lex(inp):
    it = iter(inp)
    c = next(it)
    while c is not None:
        if c == '\n':
            c = next(it, None)
        else:
            count = 0
            while c == '\t':
                count += 1
                c = next(it, None)
            length = 0
            is_file = False
            while c != '\t' and c != '\n' and c is not None:
                if c == '.':
                    is_file = True
                length += 1
                c = next(it, None)
            yield (count, length, is_file)

# faster to write, but less efficient
def lex(inp):
    tokens = inp.split('\n')
    res = []
    for t in tokens:
        h = t.count('\t')
        l = len(t) - h
        is_file = '.' in t
        res.append((t.count('\t'), l, is_file))
    return res

class Solution:
    def lengthLongestPath(self, input):
        s = []
        res = 0
        for (h, l, is_file) in lex(input):
            if len(s) == h:
                s.append(l)
            else:
                s[h] = l
            if is_file:
                res = max(res, sum(s[:h+1]) + h)
        return res
