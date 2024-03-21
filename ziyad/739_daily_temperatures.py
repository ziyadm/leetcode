"""
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to
wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
"""

from typing import List

"""
    Ziyad's Notes:
    - if we look at each value, we can see which "previous" values it is now "higher than"
    - if we keep track of the "new highest" values we see, we can know how many days that "new highest" value
    is a warmer day then
    - we can do this using a stack of the new highest days

    Analysis:
    - time complexity: O(n), add each element to a stack at most once, pop off once
    - space complexity: O(n), max stack size is all elements in the list

"""
from typing import List
import unittest

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days_to_wait = [0] * len(temperatures)
        cur_day = 0
        stack = []

        while cur_day < len(temperatures):
            while temperatures[cur_day] > temperatures[stack[-1]]:
                days_to_wait[stack[-1]] = cur_day - stack[-1]
                stack.pop()
            else:
                stack.append(cur_day)
            cur_day += 1

        return days_to_wait


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_increasing_and_decreasing_tempearture(self):
        self.assertEquals(solution.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]), [1,1,4,2,1,1,0,0])

    def test_always_increasing_temperature(self):
        self.assertEquals(solution.dailyTemperatures(temperatures = [1,2,3]), [1,1,0])
        
    def test_always_decreasing_temperature(self):
        self.assertEquals(solution.dailyTemperatures(temperatures = [3,2,1]), [0,0,0])