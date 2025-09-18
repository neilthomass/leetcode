# Last updated: 9/17/2025, 6:07:49 PM
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        l = len(mat)
        for i in range(len(mat)):
            s += mat[i][i] + mat[l - 1 - i][i]
        if l % 2 == 1:
            s -= mat[l//2][l//2]
        return s

            
        