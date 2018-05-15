# TAGS data structure, heap

# dynamic k-select
# other version: use augmented BST to get k element

import heapq


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []
        self.right = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not self.left:
            self.left.append(num)
        elif num < self.left[0]:
            heapq.heappush(self.right, -num)
        else:
            heapq.heappush(self.left, num)
        if len(self.left) < len(self.right):
            heapq.heappush(self.left, -heapq.heappop(self.right))
        elif len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.left) > len(self.right):
            return self.left[0]
        else:
            return (self.left[0] - self.right[0]) / 2
