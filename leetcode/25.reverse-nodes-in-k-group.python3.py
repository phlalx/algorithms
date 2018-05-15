# TAGS list
# TODO this was a bit tedious, there may be a more elegant solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x, next = None):
#         self.val = x
#         self.next = next


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k <= 1:
            return head

        dummy = ListNode(None)

        last = dummy  # we will chain every reversed list to 'last' element
        res = dummy
        cur = head
        undo_last_reverse = False

        while cur:

            # 'k_reversed' will point to the reversed fragment
            # we initialize it to head instead of None because we need to
            # keep track of the last element of the reversed fragment
            k_reversed = cur
            cur = cur.next
            cur_last = k_reversed
            i = 1
            while cur and i < k:
                cur_next = cur.next
                cur.next = k_reversed
                k_reversed = cur
                cur = cur_next
                i += 1
            last.next = k_reversed
            old_last = last
            last = cur_last

            if i < k:
                undo_last_reverse = True

        last.next = None

        # We don't know the length of the list, so we lazily reverse the last
        # fragment and re-reverse it if we realize its size isn't k.
        # Alternatively, we could compute the list length before hand but
        # it'll require two passes.
        if undo_last_reverse:
            cur = old_last.next
            k_reversed = None
            while cur:
                cur_next = cur.next
                cur.next = k_reversed
                k_reversed = cur
                cur = cur_next
            old_last.next = k_reversed

        return res.next
