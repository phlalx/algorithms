#TAGS binary search

import random
import bisect

class Solution:

    def __init__(self, w: List[int]):
      prefix = [0]
      for x in w:
        prefix.append(x + prefix[-1])
      self.prefix = prefix
        

    def pickIndex(self) -> int:
      y = random.randrange(1, self.prefix[-1] + 1)
      x = bisect_left(self.prefix, y, lo=1)
      return x-1
      
