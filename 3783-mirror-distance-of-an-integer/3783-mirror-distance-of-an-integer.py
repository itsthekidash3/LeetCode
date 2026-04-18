class Solution:
    def mirrorDistance(self, n: int) -> int:
        # convert n to string and return a rverse string 
        num = str(n)
        numR = num[::-1]
        return abs(n - int(numR))
        # conver to number and get the differnce


# class Solution:
#    def mirrorDistance(self, n: int) -> int:
#        rev, x=0, n
#        while x>0:
#           x, r=divmod(x, 10)
#           rev=10*rev+r
#       return abs(rev-n)     