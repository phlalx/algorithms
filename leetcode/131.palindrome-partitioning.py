#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (42.53%)
# Likes:    1332
# Dislikes: 52
# Total Accepted:    196.7K
# Total Submissions: 444.8K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
#
# Return all possible palindrome partitioning of s.
#
# Example:
#
#
# Input: "aab"
# Output:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
#
#
#
# TAGS dp, backtracking
# TODO check iterative solution https://leetcode.com/problems/palindrome-partitioning/discuss/315175/python-dp-bottom-up-beats-99.55 

# @lc code=start

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        memo = {}
        def is_pal(s, i, j):
            res = memo.get((i, j))
            if res is not None:
                return res
            if i >= j:
                res = True
            else:
                res = s[i] == s[j] and is_pal(s, i+1, j-1)
            memo[(i,j)] = res
            return res

        res = []
        cur = []
        n = len(s)
        def f(i):
            if i == n:
                res.append(list(cur))
            else:
                for j in range(i, n):
                    if is_pal(s, i, j):
                        cur.append(s[i:j+1])
                        f(j+1)
                        cur.pop()
        f(0)
        return res


# @lc code=end

