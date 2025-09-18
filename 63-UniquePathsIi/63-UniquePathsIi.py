# Last updated: 9/17/2025, 6:09:16 PM
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dirs = [(1,0),(0,1)]
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        @cache
        def helper(i,j):
            if i >= m or j >= n or obstacleGrid[i][j] == 1:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            return helper(i + 1,j)+ helper(i,j+1)
    




        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        return helper(0,0)



        
        