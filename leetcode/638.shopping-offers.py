# TAGS dynamic programming, classic
# Little trick to find an efficient recursive relation
# important to remember this trick
#
# @lc app=leetcode id=638 lang=python3
#
# [638] Shopping Offers
#
# https://leetcode.com/problems/shopping-offers/description/
#
# algorithms
# Medium (49.64%)
# Likes:    402
# Dislikes: 360
# Total Accepted:    23.7K
# Total Submissions: 47.6K
# Testcase Example:  '[2,5]\n[[3,0,5],[1,2,10]]\n[3,2]'
#
#
# In LeetCode Store, there are some kinds of items to sell. Each item has a
# price.
#
#
#
# However, there are some special offers, and a special offer consists of one
# or more different kinds of items with a sale price.
#
#
#
# You are given the each item's price, a set of special offers, and the number
# we need to buy for each item.
# The job is to output the lowest price you have to pay for exactly certain
# items as given, where you could make optimal use of the special offers.
#
#
#
# Each special offer is represented in the form of an array, the last number
# represents the price you need to pay for this special offer, other numbers
# represents how many specific items you could get if you buy this offer.
#
#
# You could use any of special offers as many times as you want.
#
# Example 1:
#
# Input: [2,5], [[3,0,5],[1,2,10]], [3,2]
# Output: 14
# Explanation:
# There are two kinds of items, A and B. Their prices are $2 and $5
# respectively.
# In special offer 1, you can pay $5 for 3A and 0B
# In special offer 2, you can pay $10 for 1A and 2B.
# You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer
# #2), and $4 for 2A.
#
#
#
# Example 2:
#
# Input: [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
# Output: 11
# Explanation:
# The price of A is $2, and $3 for B, $4 for C.
# You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C.
# You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer
# #1), and $3 for 1B, $4 for 1C.
# You cannot add more items, though only $9 for 2A ,2B and 1C.
#
#
#
# Note:
#
# There are at most 6 kinds of items, 100 special offers.
# For each item, you need to buy at most 6 of them.
# You are not allowed to buy more items than you want, even if that would lower
# the overall price.
#
#
#
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(needs)

        memo = {}

        def f(needs):
            res = memo.get(tuple(needs))
            if res is not None:
                return res


            # Correct but sub-optimal and useless
            # for i in range(n):
            #     if needs[i] > 0:
            #         new_needs = needs.copy()
            #         new_needs[i] -= 1
            #         res = min(res, f(new_needs) + price[i])
            #
            # I was trying to capture path of the form
            # -- buy one item -> special offer -> buy one item ...
            # but we don't lose any generality if we consider that
            # buying all the items at once can always be the last
            # transaction.
            # We consider the traces
            # -- offer1 ---> offer2 --> buy_everything_remaining -> done

            # price without any special offer
            res = sum(need * p for need, p in zip(needs, price)) # pythonic

            for offer in special:
                new_needs = [n - o for n, o in zip(needs, offer)] # pythonic
                if min(new_needs) >= 0:
                    res = min(res, f(new_needs) + offer[-1])

            memo[tuple(needs)] = res
            return res

        return f(needs)

