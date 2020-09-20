#bst
# boring
# corner cases
# todo we could store the distance in the queue, and
# use the grid to store the seen elements

from collections import deque

class Solution:
  def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    n = len(grid)
    if grid[0][0] == 1:
        return -1
    
    def neighs(pos):
      i, j = pos
      for di, dj in zip([0,1,0,-1,-1,1,1,-1], [1,0,-1,0,-1,1,-1,1]):
        ii = i + di
        jj = j + dj
        if 0 <= ii < n and 0 <= jj < n and grid[ii][jj] == 0:
          yield ii, jj
          
    start = 0, 0
    finish = n-1, n-1
    
    seen = {}
    
    seen[start] = 0
    dq = deque([start])
    while dq:
      pos = dq.pop()
      d = seen[pos]
      if pos == finish:
        return d + 1
      for neigh in neighs(pos):
        if neigh in seen:
          continue
        seen[neigh] = d + 1
        dq.appendleft(neigh)
    return -1
      
