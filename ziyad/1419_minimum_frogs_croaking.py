"""
You are given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs,
that is, multiple frogs can croak at the same time, so multiple "croak" are mixed.
Return the minimum number of different frogs to finish all the croaks in the given string.
A valid "croak" means a frog is printing five letters 'c', 'r', 'o', 'a', and 'k' sequentially.
The frogs have to print all five letters to finish a croak.
If the given string is not a combination of a valid "croak" return -1.

Example 1:
Input: croakOfFrogs = "croakcroak"
Output: 1
Explanation: One frog yelling "croak" twice.

Example 2:
Input: croakOfFrogs = "crcoakroak"
Output: 2
Explanation: The minimum number of frogs is two.
The first frog could yell "crcoakroak".
The second frog could yell later "crcoakroak".

Example 3:
Input: croakOfFrogs = "croakcrook"
Output: -1
Explanation: The given string is an invalid combination of "croak" from different frogs.
"""
from typing import List
from collections import defaultdict

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        frequencies = defaultdict(int)
        max_frogs = 0
        cur_frogs = 0

        for char in croakOfFrogs:
            frequencies[char] += 1

            if (frequencies['c'] >= frequencies['r'] >= frequencies['o'] >= frequencies['a'] >= frequencies['k']):
                if char == 'c':
                    cur_frogs += 1
                elif char == 'k':
                    cur_frogs -= 1
                max_frogs = max(max_frogs, cur_frogs)
            else:
                return -1

        if not (frequencies['c'] == frequencies['r'] == frequencies['o'] == frequencies['a'] == frequencies['k']):
            return -1
        
        return max_frogs


# Tests
solution = Solution()
assert solution.minNumberOfFrogs(croakOfFrogs = "croakcroak") == 1
assert solution.minNumberOfFrogs(croakOfFrogs = "crcoakroak") == 2
assert solution.minNumberOfFrogs(croakOfFrogs = "croakcrook") == -1