#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#
# https://leetcode.com/problems/binary-subarrays-with-sum/description/
#
# algorithms
# Medium (39.32%)
# Likes:    351
# Dislikes: 20
# Total Accepted:    15.7K
# Total Submissions: 38.3K
# Testcase Example:  '[1,0,1,0,1]\n2'
#
# In an array A of 0s and 1s, how many non-empty subarrays have sum S?
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [1,0,1,0,1], S = 2
# Output: 4
# Explanation: 
# The 4 subarrays are bolded below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# 
# 
# 
# 
# Note:
# 
# 
# A.length <= 30000
# 0 <= S <= A.length
# A[i] is either 0 or 1.
# 
#

# @lc code=start
#TAGS 2-sum
from collections import Counter

class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        counter = Counter()
        counter[0] = 1
        cur_sum = 0
        res = 0
        for v in A:
            cur_sum += v
            res += counter[cur_sum - S]
            counter[cur_sum] += 1
        return res


        
# @lc code=end

