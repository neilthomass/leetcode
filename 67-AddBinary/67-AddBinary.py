# Last updated: 9/17/2025, 6:09:17 PM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = int(a,2) + int(b,2) 
        t = ""
        while i:
            t = str(i % 2) + t
            i //=2
        return t or "0"