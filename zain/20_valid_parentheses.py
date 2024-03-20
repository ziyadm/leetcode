class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {'}' : '{', ')' : '(', ']':'['}

        for character in s:
            if character in close_to_open:
                if stack and stack[-1] == close_to_open[character]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)
        
        return not stack
