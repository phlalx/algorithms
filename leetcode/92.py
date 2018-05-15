#TAGS linked list
# classic
#
# Trick: Draw state before/after loop


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(next=head)
        cur = dummy
        for _ in range(m-1):
            cur = cur.next
        pre = cur
        reversed = pre.next
        last = reversed
        cur = reversed.next

        for _ in range(n-m):
            #Pythonic: Careful, order of operation is still relevant
            reversed, cur, reversed.next = cur, cur.next, reversed
            # WRONG reversed, cur, cur.next = cur, cur.next, reversed
        pre.next = reversed
        last.next = cur
        return dummy.next
        
