#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (36.36%)
# Likes:    1222
# Dislikes: 72
# Total Accepted:    287.1K
# Total Submissions: 773K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Remove all elements from a linked list of integers that have value val.
#
# Example:
#
#
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#TAGS simple linked list

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        res = ListNode()
        sol = res
        cur = head
        while cur is not None:
            if cur.val != val:
                res.next = cur
                res = cur
            cur = cur.next
        res.next = None
        return sol.next

# @lc code=end

