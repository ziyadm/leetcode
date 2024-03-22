"""
Given a string s, return the maximum number of occurrences of any substring under the following rules:
-The number of unique characters in the substring must be less than or equal to maxLetters.
- The substring size must be between minSize and maxSize inclusive.
 
Example 1:
Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
Explanation: Substring "aab" has 2 occurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).

Example 2:
Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
Output: 2
Explanation: Substring "aaa" occur 2 times in the string. It can overlap.

Constraints:
1 <= s.length <= 105
1 <= maxLetters <= 26
1 <= minSize <= maxSize <= min(26, s.length)
s consists of only lowercase English letters.
"""

"""
    Ziyad's Notes:
    - seems like we could use two nested for loops, generate all possible substrings

    Complexity:
    - Time, O(n)
    - Space, O(n)
"""

from collections import defaultdict
from typing import List
import unittest

debug = True

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        string_frequencies = defaultdict(int)
        max_substring_frequency = 0

        for start_index in range(len(s)):
            end_index = start_index
            char_frequencies = defaultdict(int)

            0, 0 + 3, 0, 1, 2
            while end_index < start_index + minSize and end_index < len(s):
                char_frequencies[s[end_index]] += 1
                end_index += 1

            if len(char_frequencies) <= maxLetters and (end_index - start_index >= minSize):
                string_frequencies[s[start_index:end_index]] += 1

            max_substring_frequency = max(max_substring_frequency, string_frequencies[s[start_index:end_index]])

        return max_substring_frequency

 
class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def skip_test_overlapping_substring(self):
        self.assertEqual(self.solution.maxFreq(s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3), 2)

    def skip_test_non_overlapping_substring(self):
        self.assertEqual(self.solution.maxFreq(s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4), 2)

    def test_non_overlapping_substring(self):
        self.assertEqual(self.solution.maxFreq(s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3), 0)

if __name__ == '__main__':
    unittest.main()