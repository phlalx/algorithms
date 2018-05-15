# TAGS grid

# O(n*m), constant space.
# TODO: can we do only one pass on the matrix?


def bordersPerSequence(line):
    res = 0
    prev = 0  # status of previous cell
    for cell in line:
        if prev != cell:
            res += 1
        prev = cell
    if prev:
        res += 1
    return res


class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = sum(bordersPerSequence(line) for line in grid)

        # we would like to apply the same treatment to the transpose
        # matrix.
        # Instead of transposing the matrix, we use generator expression
        # for cols

        for j in range(len(grid[0])):
            col = (grid[i][j] for i in range(len(grid)))
            res += bordersPerSequence(col)
        return res
