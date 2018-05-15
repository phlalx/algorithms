# TAGS cool, new, TODO broken
#
#   See 503  for getMaxNumber
#
#   Common reasoning pattern:
#   if S is a solution, so S is a combination of Left and Right, where Left
#   is a solution of nums1 for some i, and Right is a solution of nums2 for some
#   j where i + j == n
#
#   So we find the solutions to the sub-problems  and combine them to get the
#   best solution overall.
#
# See for instance https://leetcode.com/problems/create-maximum-number/discuss/77291/Share-my-Python-solution-with-explanation
#
def removeKdigits(num: str, k: int) -> str:
    res_len = len(num) - k
    st = []

    for v in num:
        while st and st[-1] < v and k > 0 and not (v == 0 and len(st) == 1):
            st.pop()
            k -= 1
        st.append(v)

    res = ''.join(st)[:res_len].lstrip('0')
    return res if res else '0'

def merge(a1, a2):
    return ''.join(sorted(list(a1) + list(a2)))

class Solution:
    # def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
    #     return 0
    def maxNumber(self, nums1, nums2, k):
        n1 = len(nums1)
        n2 = len(nums2)
        res = 0
        for i in range(k):
            if i <= n1 and 0 <= k - i <= n2:
                a1 = removeKdigits(nums1, i)
                a2 = removeKdigits(nums2, k - i)
                m = merge(a1, a2)
                res = max(res, m)
        return res

