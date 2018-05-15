#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#
# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
#
# algorithms
# Easy (48.61%)
# Likes:    471
# Dislikes: 177
# Total Accepted:    75.4K
# Total Submissions: 152.1K
# Testcase Example:  '["Shogun","Tapioca Express","Burger King","KFC"]\n' +
#  '["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]'
#
# 
# Suppose Andy and Doris want to choose a restaurant for dinner, and they both
# have a list of favorite restaurants represented by strings. 
# 
# 
# You need to help them find out their common interest with the least list
# index sum. If there is a choice tie between answers, output all of them with
# no order requirement. You could assume there always exists an answer.
# 
# 
# 
# Example 1:
# 
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
# 
# 
# 
# Example 2:
# 
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is
# "Shogun" with index sum 1 (0+1).
# 
# 
# 
# 
# Note:
# 
# The length of both lists will be in the range of [1, 1000].
# The length of strings in both lists will be in the range of [1, 30].
# The index is starting from 0 to the list length minus 1.
# No duplicates in both lists.
# 
# 
#

#TAGS set intersection
# Very cool, a variant on set intersection (need to use a map to store the
# index)

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l = { w : i for i, w in enumerate(list1) }
        res = []
        best = float('inf')
        for i, w in enumerate(list2):
            j = l.get(w)
            if j is not None and i + j <= best:
                index = i + j
                if not res or index == best:
                    res.append(w)
                else:
                    res = [w]
                best = index
        return res

# @lc code=end

# Set intersection

a = [1, 2, 4, 7]
b = [3, 7, 9, 10]

