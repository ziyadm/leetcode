"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)

        for num in nums:
            frequencies[num] += 1

        frequency_counts_of_numbers = [(num, frequency) for num, frequency in frequencies.items()]
        frequency_counts_of_numbers.sort(key = lambda num_and_frequency: num_and_frequency[1], reverse=True)
        return list(map(lambda num_and_frequency: num_and_frequency[0], frequency_counts_of_numbers[:k]))

solution = Solution()
assert solution.topKFrequent(nums = [1,1,1,2,2,3], k = 2)
assert solution.topKFrequent(nums = [1], k = 1) == [1]
