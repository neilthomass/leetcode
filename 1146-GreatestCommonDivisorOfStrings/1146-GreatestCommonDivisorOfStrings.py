# Last updated: 9/17/2025, 6:08:00 PM
import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        gcd = math.gcd(l1,l2)
        a = str1[:gcd]
        if str2 == a * (l2 // gcd) and str1 == a * (l1 // gcd):
            return a
        return ""

        
        

        