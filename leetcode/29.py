#TAGS binary search, euclidean division
# TODO not the right implementation

# interesting fact about division/modulo
# http://python-history.blogspot.com/2010/08/why-pythons-integer-division-floors.html
# https://torstencurdt.com/tech/posts/modulo-of-negative-numbers/
# pythonic  a = q.b + r  with 0 <= r < b if b > 0 
# pythonic  a = q.b + r  with 0 >= r > b else b < 0 
# q = floor(a/b)
# Pros: less surprise when restricting a value to some array bounds
# e.g. A[-1 % len(A)] 
# 
#  
# in C (and most languages) a = q.b + r  with 0 <= |r| < |b|
# q is truncated toward 0
# Pros: usual properties we have over floats

def binary(pred, i ,j):
  while i < j:
    m = (i + j) // 2
    if pred(m):
      j = m
    else:
      i = m + 1
  return i


class Solution:
  def divide(self, dividend: int, divisor: int) -> int:
    if dividend == -2147483648 and divisor == -1:
        return 2147483647
    sign = 1
    if dividend < 0:
      dividend = -dividend
      sign = -sign
    if divisor < 0:
      divisor = -divisor
      sign = -sign
    pred = lambda x: divisor * x > dividend
    res = binary(pred, 0, dividend+1)
    return sign * (res-1)
    
        
