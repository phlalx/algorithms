#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (48.72%)
# Likes:    2809
# Dislikes: 409
# Total Accepted:    726K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        first = ListNode(None)  # dummy
        last = first
        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            last.next = l1
            last = l1
            l1 = l1.next
        if l1 is None:
            l1, l2 = l2, l1
        last.next = l1
        return first.next

        
# @lc code=end

