#TAGS prefix sums, range query

# If we want to change the matrix in-place, we can't use a sentinel
# and we need to deal with corner cases

def get(matrix, i ,j):
  return 0 if i < 0 or j < 0 else matrix[i][j]

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
      if not matrix or not matrix[0]:
        return
      n = len(matrix)
      p = len(matrix[0])

      # other option here, two times prefix sum
      for i in range(n):
        for j in range(p):
          matrix[i][j] += get(matrix, i-1, j) + get(matrix, i, j-1) - get(matrix, i-1, j-1)
      self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
      a = get(self.matrix, row2, col2)
      b = get(self.matrix, row1-1, col1-1)
      c = get(self.matrix, row2, col1-1)
      d = get(self.matrix, row1-1, col2)
      return a + b - c - d



