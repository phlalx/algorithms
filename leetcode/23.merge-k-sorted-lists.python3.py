# TAGS heap, priority queue, cool
import itertools

# n is length of lists
# p is total number of elements
# O(n + p * log(n))

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


import heapq


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # trick, add counter in the heap, because < not supported on ListNode
        heap = [(l.val, count, l) for l, count in zip(lists, itertools.count()) if l]  # pythonic
        heapq.heapify(heap)  # O(n)
        res = ListNode(None)  # dummy, useful when appending at end of list
        last = res
        while heap:
            _, count, l = heapq.heappop(heap)
            if l.next:  # add tail to priority queue
                heapq.heappush(heap, (l.next.val, count, l.next))
                l.next = None
            last.next = l
            last = last.next
        return res.next
