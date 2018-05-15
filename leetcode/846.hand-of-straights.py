#TAGS map, cool
#
# Trick: greedy, use a ds to store all elements
#        find smallest element, then remove element and W successors
#
# take away:
#
#  we need a datastructure where we can remove elements and find min
#  BST would work
#  here we use map + sorted list of keys (lazy removal)
#  we could also use map + heapq if we were to insert new elements
#  dynamically. Issue is that findMin can be slow.
#
# Note: lazy removal
#
# Whenever we get the min from the sorted array, we check if it is still
# in the dictionary

from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        n = len(hand)
        if n % W != 0:
            return False
        c = Counter(hand)
        hand.sort()
        for x in hand:
            if not c[x]:
                continue
            for i in range(W):
                if c[x + i] == 0:
                    return False
                c[x + i] -= 1
        return True

# Other solution: use an Orderedict
# take away: Orderdict is like a dict, except that that popItem
#            can pop at front. Also reversed(od) is defined, and pop
#            is in constant time
# Think dict <-> stack (since python3.7)
#      ordereddict <-> deque

from collections import OrderedDict

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        n = len(hand)
        if n % W != 0:
            return False
        hand.sort()
        c = OrderedDict()
        for v in hand:
            count = c.get(v, 0)
            c[v] = count + 1
        while c:
            x = next(iter(c))
            for i in range(W):
                if x + i not in c:
                    return False
                c[x + i] -= 1
                if c[x + i] == 0:
                    c.pop(x+i)
        return True

# We don't even need an orderdict, because since python3, regular dict
# maintain element order, and we don't need to pop at the end

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        n = len(hand)
        if n % W != 0:
            return False
        hand.sort()
        c = Counter(hand)
        while c:
            x = next(iter(c)) # pythonic: retrieve element without popping
            for i in range(W):
                if x + i not in c:
                    return False
                c[x + i] -= 1
                if c[x + i] == 0:
                    c.pop(x + i)
        return True
