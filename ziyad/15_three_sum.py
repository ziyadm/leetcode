"""
Given an integer array nums,
return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""
from typing import List

cclass Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        solutions = set()

        for midpoint in range(len(nums)):
            left, right = 0, len(nums) - 1
            while left < right:
                if nums[left] + nums[midpoint] + nums[right] == 0 and \
                    left != right and left != midpoint and midpoint != right:
                    solutions.add(tuple(sorted([nums[left], nums[midpoint], nums[right]])))
                    left += 1
                    right -= 1
                elif nums[left] + nums[midpoint] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1

        return sorted(list(map(lambda solution: list(solution), solutions)))

# Tests
solution = Solution()
assert solution.threeSum(nums = [-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
assert solution.threeSum(nums = [0,1,1]) == []
assert solution.threeSum(nums = [0,0,0]) == [[0, 0, 0]]