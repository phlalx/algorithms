#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (32.14%)
# Likes:    2814
# Dislikes: 68
# Total Accepted:    222.9K
# Total Submissions: 667.5K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
#
#
#
#
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
#
#
#
#
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
#
#
#
# Example:
#
#
# Input: [2,1,5,6,2,3]
# Output: 10
#
#
#
# @lc code=start

#TAGS monotonic stack, divide/conquer, segment tree
#
# This is a very classic monotonic stack problem
# Remember this: for each j, we want to find the neart i such that
#  a_i < a_j.

# The divide/conquer solution is pretty cool
# We don't cut in the middle, but at the min, because we know how to
# conquer from this division.
# complexity is O(n^2) with naive min, O(n.log(n)) using range-min query

# range-min query is hard to get right
#
# This is conceptually very simple but tricky to implement because of
# range-min

# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         n = len(heights)
#         if not n:
#             return 0

#         # TODO what is the size of this tree?
#         tree = [ None for _ in range(4 * n) ]
#         # define these macros right away
#         left = lambda i: 2 * i + 1
#         right = lambda i: 2 * i + 2
#         root = 0

#         # TODO compare this tree with a tree produced by binary search
#         #      we cut in two adjacent parts, and not in three
#         def build_tree(i, j, node):
#             assert 0 <= i <= j <= n - 1
#             if i < j:
#                 m = (i + j) // 2
#                 build_tree(i, m, left(node))
#                 build_tree(m+1, j, right(node))
#                 tree[node] = min(tree[left(node)], tree[right(node)], key=lambda x: x[1])
#             else:
#                 # recursion stops at length 1 intervals
#                 assert i == j
#                 tree[node] = i, heights[i]

#         build_tree(0, n-1, root)

#         # We need to store the bounds of the tree, not only the query
#         def hist_min(i, j, ti, tj, node):
#             assert ti <= i <= j <= tj
#             if (i, j) == (ti, tj):
#                 return tree[node]
#             m = (ti + tj) // 2  # Not (i + j) // 2
#             if j <= m:
#                 return hist_min(i, j, ti, m, left(node))
#             elif i >= m + 1:
#                 return hist_min(i, j, m+1, tj, right(node))
#             else:
#                 return min(hist_min(i, m, ti, m, left(node)),
#                            hist_min(m+1, j, m+1, tj, right(node)), key=lambda x: x[1])
#             assert 0

#         def f(i, j):
#             if i <= j:
#                 min_i, min_v = hist_min(i, j, 0, n-1, root)
#                 return max(f(i, min_i - 1), f(min_i + 1, j), min_v * (j - i + 1))
#             else:
#                 return 0

#         return f(0, n - 1)

# It took me a while to get the "monotonic stack" answer
#
# Some tricks:
#  - for each i
#     - WRONG compute the best rectangle that ends in i (my first idea)
#     - compute the best rectangle which contains bar i
#
#  First solution O(n^2), for each i, find first elt on the left with height
#  smaller than heights[i], and first elt on the right
#
#  Trick, we can compute recursively the arrays leftFrom[i], rightFrom[i]
#  Think KMP (TODO why is this linear though?)
#
#  Better implementation, use a monotonic, increasing, stack
#  When we add a smaller element, we know the rightFrom element and can compute
#  the best surface for all elts on the stack
#
#  - Trick: need to access index/value of seen elements, so only store index
#
#       I
#     I I I
#   I I I I
#   0 1 2 3

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [-1]
        best = 0
        heights.append(0)
        for j, v in enumerate(heights):
            while st and heights[st[-1]] > v:
                height = heights[st.pop()]
                i = st[-1]
                best = max(best, (j - i - 1) * height)
            st.append(j)
        return best

# @lc code=end

