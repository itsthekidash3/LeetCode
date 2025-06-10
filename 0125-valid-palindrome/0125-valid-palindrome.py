class Solution:
    def isPalindrome(self, s: str) -> bool:
        left , right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1 #update and hold
            while left < right and not s[right].isalnum(): #skip special characters
                right -= 1 #update and hold
            
            if s[left].lower() != s[right].lower(): #lowering the char
                return False
            

            left += 1
            right -= 1

        return True





        
        