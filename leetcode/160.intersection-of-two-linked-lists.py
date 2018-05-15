# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# O(n) space solution
# store seen nodes from the first list
#
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        cur = headA
        seen = set()
        while cur is not None:
            seen.add(id(cur))
            cur = cur.next
        cur = headB
        while cur is not None:
            if id(cur) in seen:
                return cur
            cur = cur.next
        return None

# O(1) solution
# We want to walk list such that they reach intersection at the same time
#
# X -> X -> X ->
#                 X -> X
#      X -> X ->
#
# We simple precompute the lengths difference
# trick!

def length(l):
    res = 0
    while l is not None:
        l = l.next
        res += 1
    return res

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        la = length(headA)
        lb = length(headB)
        if la > lb:
            la, lb = lb, la
            headA, headB = headB, headA
        assert la <= lb
        skip = lb - la
        for _ in range(skip):
            headB = headB.next
        for _ in range(la):
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
