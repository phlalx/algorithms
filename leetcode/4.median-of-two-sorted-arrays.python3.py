#TAGS median

# Trick: kselect for two *sorted* arrays, divide and conquer
#
#  |    A   |    A   |
#  |    B       |     B     |
#           m   mm
#
#
#
#
#
#
# TODO https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2652/Share-one-divide-and-conquer-O(log(m%2Bn))-method-with-clear-description
#
# find the kth element int the two sorted arrays
# let us say: A[aMid] <= B[bMid], x: mid len of a, y: mid len of b, then wen can know
    # //
    # // (1) there will be at least (x + 1 + y) elements before bMid
    # // (2) there will be at least (m - x - 1 + n - y) = m + n - (x + y +1) elements after aMid
    # // therefore
    # // if k <= x + y + 1, find the kth element in a and b, but unconsidering bMid and its suffix
    # // if k > x + y + 1, find the k - (x + 1) th element in a and b, but unconsidering aMid and its prefix


def kselect(A, B, i, j, ii, jj, k):


    return sorted(A+B)[k]



class Solution:

    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        na = len(A)
        nb = len(B)
        k = (na + nb - 1) // 2
        if (na + nb) % 2 == 1:
            return kselect(A, B, 0, na-1, 0, nb-1, k)
        else:
            return sum(kselect(A, B, 0, na-1, 0, nb-1, u) for u in {k, k+1}) / 2
