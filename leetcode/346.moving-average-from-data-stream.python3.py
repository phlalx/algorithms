# TAGS queue, data structure

from collections import deque


class MovingAverage:
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.queue = deque()
        self.cur_sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        self.cur_sum += val
        if len(self.queue) > self.size:
            last_val = self.queue.popleft()
            self.cur_sum -= last_val
        return self.cur_sum / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
