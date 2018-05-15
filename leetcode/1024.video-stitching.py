#
# @lc app=leetcode id=1024 lang=python3
#
# [1024] Video Stitching
#
# https://leetcode.com/problems/video-stitching/description/
#
# algorithms
# Medium (48.74%)
# Likes:    428
# Dislikes: 21
# Total Accepted:    21.1K
# Total Submissions: 43.3K
# Testcase Example:  '[[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]\n10'
#
# You are given a series of video clips from a sporting event that lasted T
# seconds.  These video clips can be overlapping with each other and have
# varied lengths.
#
# Each video clip clips[i] is an interval: it starts at time clips[i][0] and
# ends at time clips[i][1].  We can cut these clips into segments freely: for
# example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].
#
# Return the minimum number of clips needed so that we can cut the clips into
# segments that cover the entire sporting event ([0, T]).  If the task is
# impossible, return -1.
#
#
#
# Example 1:
#
#
# Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
# Output: 3
# Explanation:
# We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
# Then, we can reconstruct the sporting event as follows:
# We cut [1,9] into segments [1,2] + [2,8] + [8,9].
# Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event
# [0, 10].
#
#
# Example 2:
#
#
# Input: clips = [[0,1],[1,2]], T = 5
# Output: -1
# Explanation:
# We can't cover [0,5] with only [0,1] and [0,2].
#
#
# Example 3:
#
#
# Input: clips =
# [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]],
# T = 9
# Output: 3
# Explanation:
# We can take clips [0,4], [4,7], and [6,9].
#
#
# Example 4:
#
#
# Input: clips = [[0,4],[2,8]], T = 5
# Output: 2
# Explanation:
# Notice you can have extra video after the event ends.
#
#
#
# Constraints:
#
#
# 1 <= clips.length <= 100
# 0 <= clips[i][0] <= clips[i][1] <= 100
# 0 <= T <= 100
#
#
#


# TAGS dp, greedy
# dp solution is suboptimal.

# @lc code=start
import functools

# Dp solution
# class Solution_dp:
#     def videoStitching(self, clips: List[List[int]], T: int) -> int:
#         n = len(clips)
#         clips.sort()
#         @functools.lru_cache()
#         def f(i, a):
#             # min number of clips in [i, n) to cover [a, T]
#             if a >= T:
#                 return 0
#             elif i == n or clips[i][0] > a:
#                 return float('inf')
#             else:
#                 return min(1+f(i+1, max(clips[i][1], a)), f(i+1, a))

#         res = f(0, 0)
#         if res == float('inf'):
#             return -1
#         else:
#             return res

# TODO rewrite this with a for loop over intervals

class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        n = len(clips)
        clips.sort()

        to_cover = 0  # left bound of interval to covers
        i = 0  # next clip to consider
        res = 0
        while to_cover < T and i < n:
            next_to_cover = float('-inf')
            while i < n and clips[i][0] <= to_cover:
                next_to_cover = max(next_to_cover, clips[i][1])
                i += 1
            if next_to_cover <= to_cover:
                break
            to_cover = next_to_cover
            res += 1
        return res if to_cover >= T else -1


# @lc code=end

