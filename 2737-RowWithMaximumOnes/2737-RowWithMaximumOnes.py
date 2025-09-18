# Last updated: 9/17/2025, 6:07:36 PM
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        rows = []

        for i in range(len(mat)):

            rows.append([i,sum(mat[i])])
        return max(rows,key = lambda x: x[1])