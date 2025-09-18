# Last updated: 9/17/2025, 6:07:47 PM
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m = 0
        for l in accounts:
            m = max(m,sum(l))
        return m

        