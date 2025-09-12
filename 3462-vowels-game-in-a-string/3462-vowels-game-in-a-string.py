class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for v in "aeiou":
            #if there are odd number of vowels
            if v in s:
                return True 
        
        else: #if there are even number of vowels. 
        #if alice removes odd from even substring , alice wins since theres an guarnatee that theres gonna be odd number of vowels left
            return False