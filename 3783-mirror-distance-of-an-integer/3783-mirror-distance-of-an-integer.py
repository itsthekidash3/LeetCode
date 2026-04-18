class Solution:
    def mirrorDistance(self, n: int) -> int:
        # convert n to string and return a rverse string 
        num = str(n)
        numR = num[::-1]
        return abs(n - int(numR))
        # conver to number and get the differnce
        