"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
 

Constraints:
1 <= n <= 8
"""
from typing import List
import unittest

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        valid_parentheses = []

        def generate_valid_parentheses(so_far: str, remaining_opens: int, remaining_closes: int):
            if remaining_closes == 0 and remaining_opens == 0:
                valid_parentheses.append(so_far)
            if remaining_opens > 0:
                generate_valid_parentheses(so_far + "(", remaining_opens=remaining_opens-1, remaining_closes=remaining_closes)
            if remaining_closes > remaining_opens:
                generate_valid_parentheses(so_far + ")", remaining_opens=remaining_opens, remaining_closes=remaining_closes-1)

        generate_valid_parentheses("", remaining_opens=n, remaining_closes=n)
        return valid_parentheses
        
class SolutionTest:
    def setUp(self):
        self.solution = Solution()
    
    def test_multiple_combinations(self):
        self.assertEquals(self.solution.generateParenthesis(n=n), ["((()))","(()())","(())()","()(())","()()()"])

    def single_combination(self):
        self.assertEquals(self.solution.generateParenthesis(n=1), ["()"])

    def no_combination(self):
        self.assertEquals(self.solution.generateParenthesis(n=0), [])