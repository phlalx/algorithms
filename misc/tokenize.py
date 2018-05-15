# invariant: 
#  - c points on the first not processed char
#  we need share state, c and iterator on input string

def lexer(s):
  
  chars = iter(s)
  c = next(chars, None)
 
  def lex_int():
    nonlocal c
    res = 0
    while c and c.isdigit():
      res = 10 * res + int(c)
      c = next(chars, None)
    return res

  def lex_str():
    nonlocal c
    res = []
    while c and c.isalpha():
      res.append(c)
      c = next(chars, None)
    return "".join(res)

  while c:
    if c.isdigit():
      tok = lex_int()
      yield tok
    elif c == ' ':
      c = next(chars, None)
    else:
      tok = lex_str()
      yield tok

# Version 2
def lexer(c):
    i = 0
    n = len(c)
    while i < n:
        if c[i].isdigit():
            res = 0
            while i < n and c[i].isdigit():
                res = 10 * res + int(c[i])
                i += 1
            yield res
        elif c[i] == ' ':
            i += 1
        else:
            res = ''
            while i < n and c[i].isalpha():
                res += c[i]
                i += 1
            yield res

for tok in lexer("1234 this is a test 123"):
  print(tok)
