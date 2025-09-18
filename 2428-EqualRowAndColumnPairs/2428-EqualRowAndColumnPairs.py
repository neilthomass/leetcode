# Last updated: 9/17/2025, 6:07:40 PM
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        counter = 0

        # Iterate over all rows and columns
        for row in grid:
            for col in zip(*grid):  # Use zip to extract columns
                if list(col) == row:
                    counter += 1

        return counter
