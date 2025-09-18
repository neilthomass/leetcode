# Last updated: 9/17/2025, 6:07:38 PM
class Solution:
    def partitionString(self, s: str) -> int:
        m = 1
        mySet = set()

        for c in s:
            if c in mySet:
                m += 1
                mySet.clear()
                mySet.add(c)
            else:
                mySet.add(c)
        

        return m