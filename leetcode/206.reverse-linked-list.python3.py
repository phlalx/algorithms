# TAGS list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, y=None):
        self.val = x
        self.next = y


def listToPylist(l):
    if l:
        return [l.val] + listToPylist(l.next)
    else:
        return []


def PylistToList(l):
    if l:
        return ListNode(l[0], PylistToList(l[1:]))
    else:
        return None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = None
        while head:
            old_head = head
            head = head.next
            old_res = res
            res = old_head
            res.next = old_res
        return res


sol = Solution()
l = PylistToList([1, 2, 3, 4])
r = sol.reverseList(l)
print(listToPylist(r))
