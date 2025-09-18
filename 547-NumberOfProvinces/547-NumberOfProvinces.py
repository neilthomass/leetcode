# Last updated: 9/17/2025, 6:08:14 PM
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        l = len(isConnected)



        wqu = [-1] * l

        def find(i):
            if wqu[i] == -1:
                return i
            wqu[i] = find(wqu[i])
            return wqu[i]

        def connect(i, j):
            ri = find(i)
            rj = find(j)
            if ri != rj:
                wqu[rj] = ri

        for i in range(l):
            for j in range(l):
                if isConnected[i][j]:
                    connect(i, j)

        
        return sum(1 for v in wqu if v == -1)
