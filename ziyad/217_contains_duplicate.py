"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

from collections import defaultdict
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        frequencies = defaultdict(int)

        for num in nums:
            frequencies[num] += 1

            if frequencies[num] > 1:
                return True

        return False


# Tests
solution = Solution()
assert solution.containsDuplicate(nums=[1,2,3,1])
assert not solution.containsDuplicate(nums=[1,2,3,4])
assert solution.containsDuplicate(nums=[1,1,1,3,3,4,3,2,4,2])