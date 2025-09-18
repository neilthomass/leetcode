# Last updated: 9/17/2025, 6:08:40 PM
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        @cache
        def dfs(level,i):
            if level >= len(triangle):
                return 0
            return triangle[level][i] + min(dfs(level + 1,i), dfs(level + 1, i+1))

        return dfs(0,0)

