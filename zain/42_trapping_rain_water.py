class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = 1
        total_area = 0

        while right < len(height):
            if height[left] < height[right]:
                left = right
                right += 1

            else: 
                total_area += (height[left] - height[right])
                right += 1

        return total_area      
