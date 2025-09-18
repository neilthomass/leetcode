# Last updated: 9/17/2025, 6:08:18 PM
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        d = {}
        for c in t:
            d[c] = d.get(c,0) + 1
        for c in s:
            d[c] -= 1
            if d[c] == 0:
                del d[c]
        

        return list(d.keys())[0]

        