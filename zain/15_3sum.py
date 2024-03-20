class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Key is 0 - sum, value is numbers that add up to that sum
        sums = {}

        left = 0
        right = 1
        while left < len(nums) - 1:
            sums[0 - (nums[left] + nums[right])] = (nums[left], nums[right])
            right += 1
            if right == len(nums):
                left += 1
                right = left + 1

        results = set()

        for index, value in enumerate(nums):
            if (value) in sums:
                sorted_list = [value, sums[value][0], sums[value][1]]
                sorted_list.sort()
                results.add((sorted_list[0], sorted_list[1], sorted_list[2]))
        
        return results



