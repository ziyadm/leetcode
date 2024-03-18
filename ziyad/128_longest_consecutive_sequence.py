"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_length_sequence = 0

        for num in nums:
            sequence_length = 1
            if num - 1 not in nums:
                while num + sequence_length in nums:
                    sequence_length += 1 
            max_length_sequence = max(max_length_sequence, sequence_length)

        return max_length_sequence


# Tests
solution = Solution()
assert solution.longestConsecutive(nums = [100,4,200,1,3,2]) == 4
assert solution.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]) == 9