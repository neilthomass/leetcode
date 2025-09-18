# Last updated: 9/17/2025, 6:09:28 PM
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1,len(nums)-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                left = j + 1
                right = len(nums) - 1

                while left < right:
        
                    sum = nums[i] + nums[j] + nums[right] + nums[left]

                    if sum == target:
                        ans.append([nums[i], nums[j],nums[left],nums[right]])
                        left += 1
                        right -= 1
                    
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        
                        while  left < right and nums[right] == nums[right+1]:
                            right -= 1
                    
                    elif sum < target:
                        left += 1
                    else:
                        right -= 1




        return ans