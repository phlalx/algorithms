#TAGS counting sort, buckle sort, cool
#
# Trick: count persons of a given age
# because range of age is [1,120] 
#
# Instead of doing
#  for each person, count which other persons match the constraint,
#
# we compute for each person the candidate ages, and count how many person
# have that age
# We could do even simpler, iterate over ages * ages

from collections import Counter

def pred(a, b):
    c1 = b <= 0.5 * a + 7
    c2 = b > a
    c3 = b > 100 and a < 100
    return c1 or c2 or c3

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counter = Counter(ages)
        res = 0
        for a, num in counter.items():
            request = sum(counter[b] for b in range(0, 121) if not pred(a, b))
            if not pred(a, a):
                request -= 1
            res += request * num
        return res

#  
#  class Solution:
#      def numFriendRequests(self, ages: List[int]) -> int:
#          counter = Counter(ages)
#          res = 0
#          for a, num_a in counter.items():
#              for b, num_b in counter.items():
#                  if a != b and not pred(a, b):
#                      res += num_a * num_b
#                  elif a == b and not pred(a, b):
#                      res += num_a * (num_a - 1)
#          return res
#  
