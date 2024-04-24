"""
Problem Statement:

You are given an encrypted message where the encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Your task is to decode this message.

The function will take a string as input and return a string.

Input:
s: A string

Output:
A string, representing the decoded message.

Example:

Input: "2[ab]3[cd]"
Output: "ababcdcdcd"

Input: "3[a2[b]]"
Output: "abbabbabb" 

Note:
1. s consists of lowercase English letters, digits, and square brackets '[]'.
2. s is guaranteed to be a valid input.
3. All the integers in s are in the range [1, 300].
4. The length of the output will never exceed 10^5.

"""
class Solution:
    def decode_string(self, s: str) -> str:
        stack = []
        current_num = 0
        current_string = ""
        
        for char in s:
            if char.isdigit():
                current_num = int(char)
            elif char == '[':
                stack.append(current_string)
                stack.append(current_num)
                current_string = ""
                current_num = 0
            elif char == ']':
                num = stack.pop()
                prev_string = stack.pop()
                current_string = prev_string + num * current_string
            else:
                current_string += char
        
        return current_string
    
solution = Solution()
assert solution.decode_string(s="2[ab]3[cd]") == "ababcdcdcd"
assert solution.decode_string(s="3[a2[b]]") == "abbabbabb"