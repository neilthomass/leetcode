# Last updated: 9/17/2025, 6:08:37 PM
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int: 
        if sum(cost) > sum(gas):
            return -1

        tot = 0
        start = 0

        for i in range(len(gas)):
            tot += gas[i] - cost[i]

            if tot < 0:
                start = i + 1
                tot = 0

        return start

    
        
        