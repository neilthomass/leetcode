# Last updated: 9/17/2025, 6:09:38 PM
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s

        ans = [""] * numRows
        j = 0
        inc = 1
        for i in range(len(s)):
            ans[j] += s[i]
            if j == 0:
                inc = 1
            if j == numRows - 1:
                inc = -1
            j += inc


        return "".join(ans)

        