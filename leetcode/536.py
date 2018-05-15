#TAGS parser, lexer
# Corner case: negative number
# Trees can have only left subtree

from typing import Iterator, Union

def lexer(s) -> Iterator[Union[str, int]]:
    i = 0
    n = len(s)
    while i < n:
        if s[i] in {'(',')'}:
            yield s[i]
            i += 1
        else:
            neg = False
            if s[i] == '-':
                i += 1
                neg = True
            num = int(s[i])
            i += 1
            while i < n and s[i].isdigit():
                num = 10 * num + int(s[i])
                i += 1
            yield -num if neg else num

# Recursive descent: tedious
            
class Solution:
    def str2tree(self, s: str) -> TreeNode:
      if not s:
        return None
      it = lexer(s)

      cur = next(it)
      def f():
        nonlocal cur
        num = cur
        cur = next(it, None)
        if cur == ')' or cur is None:
            return TreeNode(num)
        assert cur == '('
        cur = next(it)
        left = f()
        assert cur == ')'
        cur = next(it, None)
        if cur == '(':
            cur = next(it)
            right = f()
            assert ')' == cur
            cur = next(it, None)
        else:
            right = None
        return TreeNode(num, left, right)
      return f()

# iterative parser LR(1)!!!

class Solution:
    def str2tree(self, s: str) -> TreeNode:
      if not s:
        return None
      st = []
      for t in lexer(s + ')'):
        if isinstance(t, int):
          st.append(t)
        elif t == '(':
          continue
        elif isinstance(st[-1], int):  # t == ')'
          st[-1] = TreeNode(st[-1])
        elif isinstance(st[-2], TreeNode):
          t1 = st.pop()
          t2 = st.pop()
          st[-1] = TreeNode(st[-1], t2, t1)
        else:
          t = st.pop()
          st[-1] = TreeNode(st[-1], t)
      return st[-1]
      
