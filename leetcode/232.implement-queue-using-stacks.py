#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#
# https://leetcode.com/problems/implement-queue-using-stacks/description/
#
# algorithms
# Easy (44.73%)
# Likes:    787
# Dislikes: 129
# Total Accepted:    184.7K
# Total Submissions: 395.8K
# Testcase Example:  '["MyQueue","push","push","peek","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# Implement the following operations of a queue using stacks.
#
#
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
#
#
# Example:
#
#
# MyQueue queue = new MyQueue();
#
# queue.push(1);
# queue.push(2);
# queue.peek();  // returns 1
# queue.pop();   // returns 1
# queue.empty(); // returns false
#
# Notes:
#
#
# You must use only standard operations of a stack -- which means only push to
# top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may
# simulate a stack by using a list or deque (double-ended queue), as long as
# you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek
# operations will be called on an empty queue).
#
#
#

# @lc code=start


class MyQueue:

    def reverse(self):
        assert not self.y
        while self.x:
            v = self.x.pop()
            self.y.append(v)

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.x = []
        self.y = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.x.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.y:
            self.reverse()
        return self.y.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.y:
            self.reverse()
        return self.y[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not (self.x or self.y)



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

