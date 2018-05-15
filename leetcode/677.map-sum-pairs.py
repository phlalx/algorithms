#
# @lc app=leetcode id=677 lang=python3
#
# [677] Map Sum Pairs
#
# https://leetcode.com/problems/map-sum-pairs/description/
#
# algorithms
# Medium (52.18%)
# Likes:    344
# Dislikes: 64
# Total Accepted:    30.5K
# Total Submissions: 58.2K
# Testcase Example:  '["MapSum", "insert", "sum", "insert", "sum"]\n' +
  '[[], ["apple",3], ["ap"], ["app",2], ["ap"]]'
#
#
# Implement a MapSum class with insert, and sum methods.
#
#
#
# For the method insert, you'll be given a pair of (string, integer). The
# string represents the key and the integer represents the value. If the key
# already existed, then the original key-value pair will be overridden to the
# new one.
#
#
#
# For the method sum, you'll be given a string representing the prefix, and you
# need to return the sum of all the pairs' value whose key starts with the
# prefix.
#
#
# Example 1:
#
# Input: insert("apple", 3), Output: Null
# Input: sum("ap"), Output: 3
# Input: insert("app", 2), Output: Null
# Input: sum("ap"), Output: 5
#
#
#
#

# @lc code=start
def tree_sum(cur):
  v = cur.get(None)
  res = 0 if v is None else v
  res += sum(tree_sum(child) for bla, child in cur.items() if bla is not None)
  return res

class MapSum:

  def __init__(self):
    self.trie = {}

  def insert(self, key, val):
    cur = self.trie
    for c in key:
      cur = cur.setdefault(c, {})
    cur[None] = val

  def sum(self, prefix):
    cur = self.trie
    for c in prefix:
      cur = cur.get(c)
      if cur is None:
        return 0
    return tree_sum(cur)



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# @lc code=end

