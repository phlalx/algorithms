# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#TAGS linked list

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = res = ListNode()
        pre.next = head
        # We want to go from pre, a, b to pre, b, a
        # pre, a, b -> pre, b, a  
        while pre.next and pre.next.next:
            a = pre.next
            b = pre.next.next
            pre.next, b.next, a.next = b, a, b.next  # pythonic
            pre = a
        return res.next

