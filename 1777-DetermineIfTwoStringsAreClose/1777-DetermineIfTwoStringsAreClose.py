# Last updated: 9/17/2025, 6:07:50 PM
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        q = len(word1)
        if q != len(word2) or set(word1) != set(word2):
            return False
        d1,d2 = {},{}
        for i in range(q):
            c1 = word1[i]
            c2 = word2[i]
            d1[c1] = d1.get(c1,0) + 1
            d2[c2] = d2.get(c2,0) + 1
        return sorted(d1.values()) == sorted(d2.values())



        