"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            max_water = max(max_water, min(height[left], height[right]) * (right - left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water

# Tests
solution = Solution()
assert solution.maxArea(height=[1,8,6,2,5,4,8,3,7]) == 49
assert solution.maxArea(height=[1,1]) == 1