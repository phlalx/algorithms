# TAGS list datatype
# Trick:
#    for each elements, we pick up with odd 1 / i where i is the rank of the
#    element.
#
#    suppose n element (1 to n)
#      P(X = n) = 1 / n   (that's good)
#      P(X = n - 1) = (1 / (n - 1)) * (1 - 1 / n) = 1 / n
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random


class Solution:
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        cur_node = self.head
        cur_len = 1
        while cur_node:
            if random.randrange(0, cur_len) == 0:
                cur_rand = cur_node.val
            cur_len += 1
            cur_node = cur_node.next
        return cur_rand


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
