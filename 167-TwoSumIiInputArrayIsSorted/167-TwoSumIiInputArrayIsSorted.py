# Last updated: 9/17/2025, 6:08:33 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)
        

        
        left = 0
        right = n - 1
        while  left < right:
    
            s = numbers[right] + numbers[left]
            if s == target:
                return [left + 1,right + 1]
            elif s < target:
                left += 1
            else:
                right -= 1
            


        