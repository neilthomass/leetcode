# Last updated: 9/17/2025, 6:09:31 PM
class Solution:
    def threeSumClosest(self, nums: List[int],target) -> int:
        nums.sort()
        answer = float("inf")
        n = len(nums)


        if sum(nums[:3])>target:
            return sum(nums[:3])
        if sum(nums[-3:])<target:
            return sum(nums[-3:])

        for k in range(n-2):

            i = k + 1
            j = n - 1

            while i < j:

                s = nums[i] + nums[j] + nums[k] 

                if abs(s - target) < abs(answer - target):
                    answer = s
                
                if s < target:
                    i += 1
                elif s  > target:
                    j -= 1
                else:
                    return answer
        
        return answer
        