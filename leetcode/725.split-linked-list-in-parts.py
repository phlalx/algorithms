#TAGS linked list, arithmetic

#  how to find the length  of each segment?
# n = q * k + r with r in [0, k - 1]
#
# We just need to redistribute the r, which gives us
# n = q * (r + r') + r    with r + r' = k
#   = (q + 1) * r + q * (k - r) 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def extract(cur, q):
    last = ListNode(None)
    res = last
    while q > 0:
        last.next = ListNode(cur.val)
        last = last.next
        cur = cur.next
        q -= 1
    return cur, res.next

class Solution:
    def splitListToParts(self, root, k):
        cur = root
        n = 0
        while cur is not None:
            n += 1
            cur = cur.next
        q, r = n // k, n % k
        cur = root
        res = []
        for _ in range(r):
            cur, head = extract(cur, q+1)
            res.append(head)
        for _ in range(k-r):
            cur, head = extract(cur, q)
            res.append(head)
        assert cur is None
        return res
