#TAGS iterator
# trick define NextChar iterator
#

class NextChar():
  
  def __init__(self):
    self.buf = [None] * 4
    self.cur = 0
    self.last = 0
  
  def next(self):
    if self.cur < self.last: 
      res = self.buf[self.cur]
      self.cur += 1
      return res
    else:
      n_read = read4(self.buf)
      if n_read == 0:
        return None
      else:
        self.cur = 0
        self.last = n_read
        res = self.buf[self.cur]
        self.cur += 1
        return res

class Solution:

  def __init__(self):
    self.nextChar = NextChar()

  def read(self, buf, n):
    total_read = 0
    char = None
    cur = 0
    while total_read < n and (char := self.nextChar.next()) is not None:
      buf[cur] = char
      cur += 1
      total_read += 1
    return total_read
  
