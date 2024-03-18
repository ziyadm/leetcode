"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""
class Solution:
    def isValid(self, s: str) -> bool:
        parens_map = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []
        index = 0

        while index < len(s):
            if s[index] not in parens_map:
                stack.append(s[index])
            else:
                if len(stack) == 0:
                    return False
                
                if stack.pop() != parens_map[s[index]]:
                    return False
            index += 1

        return len(stack) == 0

# Tests
solution = Solution()
assert solution.isValid(s = "()")
assert solution.isValid(s = "()[]{}")
assert not solution.isValid(s = "(]")