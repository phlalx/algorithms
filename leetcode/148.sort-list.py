#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list/description/
#
# algorithms
# Medium (37.07%)
# Likes:    1795
# Dislikes: 93
# Total Accepted:    211.7K
# Total Submissions: 561K
# Testcase Example:  '[4,2,1,3]'
#
# Sort a linked list in O(n log n) time using constant space complexity.
#
# Example 1:
#
#
# Input: 4->2->1->3
# Output: 1->2->3->4
#
#
# Example 2:
#
#
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#TAGS linked list
# trick: split the list in two by using two pointers (fast, slow)
# TODO try to do it without recursion using constant space

class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        # allocate dummy node once for all
        dummy = ListNode(42)

        # merge two lists, and append nodes to res
        def merge(head1, head2, res):
            while head1 and head2:
                if head1.val <= head2.val:
                    res.next = head1
                    head1 = head1.next
                else:
                    res.next = head2
                    head2 = head2.next
                res = res.next
            res.next = head1 or head2

        def sort(head):
            if head is None or head.next is None:
                return head

            half1 = head
            half2 = head.next

            half_end = [half1, half2]

            # split list in two halves half_cur[0] and half_cur[1]
            # STUPID idea!
            #    I got the idea while misunderstanding someone's solution
            #    but it makes no sense.
            #    just find the middle of the list by keeping
            #    two pointers, one fast one slow.
            #
            cur = head
            c = 0
            while cur:
                next = cur.next
                half_end[c].next = cur
                half_end[c] = cur
                c = 0 if c else 1
                cur = next
            for c in range(2):
                half_end[c].next = None

            sorted_half1 = sort(half1)
            sorted_half2 = sort(half2)

            merge(sorted_half1, sorted_half2, dummy)

            return dummy.next

        return sort(head)

# @lc code=end

