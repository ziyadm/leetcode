"""
Problem Statement:

You are given a string 's' that consists only of alphanumeric characters and parentheses - '(', ')'. Your task is to write a function that balances the parentheses in the string by removing as few characters as possible.

The function will take an unbalanced string as input and return a new string where all parentheses are balanced, preserving the sequence of the characters.

Input:
s: A string composed of alphanumeric characters and parentheses. (1 <= len(s) <= 10^5)

Output:
A string where parentheses are balanced by removing the minimum number of characters, and the remaining characters still hold their original order in the string.

Example:

Input: "a(b(c)d)e)"
Output: "a(b(c)d)e"

Input: "(a(b(c)d"
Output: "ab(c)d"

Note:
1. If there are multiple solutions, you can return any one.
2. 'Balanced parentheses' means every opening parenthesis has a matching closing parenthesis, and vice versa.
3. The empty string is considered balanced.
    
"""


class Solution:
    def balance(self, s: str) -> str:
        left_parens = sum(1 if char == '(' else 0 for char in s)
        right_parens = sum(1 if char == ')' else 0 for char in s)
        delta = left_parens - right_parens
        remove_char = ')' if delta < 0 else '('
        delta = abs(delta)
        so_far = ""

        for char in s:
            if char == remove_char and delta > 0:
                delta -= 1
            else:
                so_far += char
        
        return so_far

solution = Solution()
print(solution.balance("a(b(c)d)e)"))
print(solution.balance("(a(b(c)d"))