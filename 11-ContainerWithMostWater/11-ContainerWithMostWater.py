# Last updated: 9/17/2025, 6:09:35 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        left, right = 0, len(height) - 1  # Initialize two pointers
        while left < right:
            # Calculate the area
            width = right - left
            current_height = min(height[left], height[right])
            maxA = max(maxA, width * current_height)

            # Move the pointer pointing to the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxA
