class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(current_area, max_area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_area
