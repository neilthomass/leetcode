# Last updated: 9/17/2025, 6:09:33 PM
class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        i = 0
        d = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in d:
                    num += d[s[i:i+2]]
                    i += 2
            else:
                num += d[s[i]]
                i += 1

        return num

        
        