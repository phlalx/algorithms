#TAGS linked list
# harder than other linked lists problem
#
# Trick:
# 1. For these linked list exercises, always wonder if we add at the end of
#    an existing list, or at the top
# 2. if complex, try to divide into smaller problems
# 3. for this problem where lists are split into two parts, always think
#    about even/odd test cases


# a and b have same number of elt, or b has one extra element
def mix_linked_lists(a: ListNode, b: ListNode) -> None:
  last = ListNode()
  while a is not None and b is not None:
    last.next = a
    a.next, a = b, a.next
    last, b = b, b.next
  assert a is None
  last.next = b
  
def reverse(a: ListNode) -> ListNode:
  cur = a
  res = None
  while cur is not None:
    cur.next, res, cur = res, cur, cur.next
  return res

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
          return head
        # head -> 1 2 3 4 5 6
        # a -> 1 2 3
        # b -> 6 5 4
        #
        # head -> 1 2 3 4 5 6 7
        # a -> 1 2 3 
        # b -> 7 6 5 4
       
        pre = ListNode()
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
          pre, slow = slow, slow.next
          fast = fast.next.next
        pre.next = None
        a = head
        b = reverse(slow)
        
        # a_first has at most one more element than b_first
        mix_linked_lists(a, b)
        return a
        
