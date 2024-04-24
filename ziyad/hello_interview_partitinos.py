"""
Problem Statement:
    
Given a string 's', your task is to partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once. Return the minimum number of substrings in such a partition.

The function will take a string as input and return an integer.

Input:
s: A string

Output:
An integer, representing the minimum number of substrings in the partition.

Example:

Input: "banana"
Output: 3 ('ban', 'an', 'a')

Input: "hhhh"
Output: 4 ('h', 'h', 'h', 'h')

Note:
1. s consists of only English lowercase letters.
2. 1 <= s.length <= 10^5.
    
"""
from collections import defaultdict
import sys

class Solution:
    def min_unique_substring_partition(self, s: str) -> int:
        partition_size = 1
        char_frequency = defaultdict(int)
        index = 0

        while index < len(s):
            char_frequency[s[index]] += 1
            if char_frequency[s[index]] > 1:
                partition_size += 1
                char_frequency = defaultdict(int)
                char_frequency[s[index]] = 1
            index += 1

        return partition_size

solution = Solution()
assert solution.min_unique_substring_partition(s="banana") == 3
assert solution.min_unique_substring_partition(s="hhhh") == 4
