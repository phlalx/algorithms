# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, p = binaryMatrix.dimensions()
        j = p - 1
        for i in range(n):
            while j >= 0 and binaryMatrix.get(i, j) == 1:
                j -= 1
        return j + 1 if j < p - 1 else -1



