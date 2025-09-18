# Last updated: 9/17/2025, 6:09:17 PM
from itertools import cycle
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        
        n = len(matrix)
        m = len(matrix[0])


        i = 0
        j = 0

        gen = cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])
        di, dj = next(gen)

        
        while len(ans) < n*m:
            ans.append(matrix[i][j])
            matrix[i][j] = -1000

            if not 0 <= i + di < n or not 0 <= j + dj < m or matrix[i + di][j + dj] == -1000:
                di, dj = next(gen)
            
            i, j = i + di, j + dj
        
        return ans
            





            









            



            
            
        return ans
