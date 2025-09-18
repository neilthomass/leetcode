# Last updated: 9/17/2025, 6:09:36 PM
class Solution:
    def myAtoi(self, s: str) -> int:


        if s == "":
            return 0
            _
        i = 0
        sign = 1
        num = 0

        while i < len(s) - 1 and s[i] == " ":
            i += 1
        
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1
        

        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        
        if num * sign < -2**31:
            return -2**31

        if num * sign > 2**31 - 1:
            return 2**31 - 1
        
        return num * sign
        





        

            
            
        