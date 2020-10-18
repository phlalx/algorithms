#TAGS circular buffer

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.nums = [None] * (k+1)
        self.i = 0  # first
        self.j = 0  # last
        self.k = k
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.i = (self.i + 1) % (self.k + 1)
        self.nums[self.i] = value
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.j = (self.j + 1) % (self.k + 1)
        return True
    

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.nums[(self.j+1) % (self.k + 1)]

    

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
  
        if self.isEmpty():
            return -1
        return self.nums[self.i]
  
    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.i == self.j
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return (self.j - self.i) % (self.k + 1) == 1 
        


