# Last updated: 9/17/2025, 6:09:34 PM
class Solution:
    def intToRoman(self, num: int) -> str:
        res = []
        dict = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
        
        for val in dict:
            if num == 0:
                break
            count = num//val
            res.append(dict[val]*count)
            num -= count * val
        
        return "".join(res)

        
        
        