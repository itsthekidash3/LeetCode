class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        l,r = 0, len(letters)
        while l < r:
            mid = l+(r-l) // 2 #mid of first half
            if letters[mid] > target:
                r = mid
            else:
                l = mid + 1 #if its at mid 
        
        if l == len(letters):
            return letters[0]
        
        return letters[l]
