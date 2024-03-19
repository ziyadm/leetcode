class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        
        for letter in s:
            if letter.isalnum():
                cleaned += letter
                
        cleaned = cleaned.lower()
        left = 0
        right = len(cleaned) - 1
        
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        
        return True
    
