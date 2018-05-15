# TAGS data structure, cool


class Node:
    def __init__(self, elt, next_node=None, node_min=None):
        self.elt = elt
        self.next_node = next_node
        self.node_min = node_min


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = None
        self.cur_min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack = Node(x, self.stack, self.cur_min)
        if not self.cur_min or x < self.cur_min.elt:
            self.cur_min = self.stack

    def pop(self):
        """
        :rtype: void
        """
        assert self.stack
        self.cur_min = self.stack.node_min
        self.stack = self.stack.next_node

    def top(self):
        """
        :rtype: int
        """
        assert self.stack
        return self.stack.elt

    def getMin(self):
        """
        :rtype: int
        """
        assert self.stack and self.cur_min
        return self.cur_min.elt
