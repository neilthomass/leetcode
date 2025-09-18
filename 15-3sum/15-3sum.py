# Last updated: 9/17/2025, 6:09:31 PM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answers = []
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]:
                continue

            i = k + 1
            j = len(nums) - 1
            while k < i < j:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    answers.append(sorted([nums[i],nums[j],nums[k]]))
                    i += 1
                    while i < j and nums[i] == nums[i-1]:
                        i +=1 
                elif sum < 0:
                    i += 1
                else:
                    j -= 1
        return answers
        