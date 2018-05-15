#TAGS matrix
#trick: no need to read diag by diag

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix or not matrix[0]:
            return True
        n = len(matrix)
        p = len(matrix[0])
        for i in range(n-1):
            for j in range(p-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True
        
