#
# @lc app=leetcode id=1171 lang=python3
#
# [1171] Remove Zero Sum Consecutive Nodes from Linked List
#
# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/description/
#
# algorithms
# Medium (43.18%)
# Likes:    159
# Dislikes: 17
# Total Accepted:    6.3K
# Total Submissions: 15K
# Testcase Example:  '[1,2,-3,3,1]'
#
# Given the head of a linked list, we repeatedly delete consecutive sequences
# of nodes that sum to 0 until there are no such sequences.
#
# After doing so, return the head of the final linked list.  You may return any
# such answer.
#
#
# (Note that in the examples below, all sequences are serializations of
# ListNode objects.)
#
# Example 1:
#
#
# Input: head = [1,2,-3,3,1]
# Output: [3,1]
# Note: The answer [1,2,1] would also be accepted.
#
#
# Example 2:
#
#
# Input: head = [1,2,3,-3,4]
# Output: [1,2,4]
#
#
# Example 3:
#
#
# Input: head = [1,2,3,-3,-2]
# Output: [1]
#
#
#
# Constraints:
#
#
# The given linked list will contain between 1 and 1000 nodes.
# Each node in the linked list has -1000 <= node.val <= 1000.
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# Examples:
#   1 -> 1 -> -1 -> 3 -> None
#   0 -> None
#   1 -> -1 -> None
#   2 -> 1 -> -1 -> -2 -> None
#
#
#   1 -> 1 -> 2 -> -2 -> -1 -> 3 -> None
#      s = 3                  s = 3
#
# TAGS cool 2-sum linked list
# good application of OrderedDict, even though there must be a different
# solution

from collections import OrderedDict

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        cur = head
        cur_sum = 0
        seen = OrderedDict({0 : dummy})

        while cur is not None:
            cur_sum += cur.val
            past_cur = seen.get(cur_sum)

            if past_cur is not None:
                past_cur.next = cur.next
                cur = past_cur
                while seen.popitem()[0] != cur_sum:
                    pass


            assert cur_sum not in seen
            seen[cur_sum] = cur

            cur = cur.next

        return dummy.next

# @lc code=end

