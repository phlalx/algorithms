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


def listLength(l):
    res = 0
    while l:
        res = res + 1
        l = l.next
    return res


def listEqual(l1, l2):
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return not l1 and not l2


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        len = listLength(head)
        if len == 1:
            return True
        reversed = None
        for _ in range(len // 2):
            reversedOld = reversed
            reversed = head
            head = head.next
            reversed.next = reversedOld
        if len % 2:  # we skip middle element
            assert head
            head = head.next

        return listEqual(reversed, head)


s = Solution()
assert s.isPalindrome(PylistToList(""))
assert s.isPalindrome(PylistToList("aba"))
assert not s.isPalindrome(PylistToList("abb"))
