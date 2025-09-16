import math

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:

        result = []

        def gcd(x,y):  #setting up the gcd
            return math.gcd(x,y)
        
        def lcm(x,y): #setting up the lcm
            if x == 0 or y == 0:
                return 0
            return abs(x*y) // gcd(x,y)
        
        for num in nums:
            result.append(num)

            while len(result) >= 2:

                x = result[-1]  #last in first out. so stack
                y = result[-2]

                common = gcd(x,y)  #looking for gcd

                if common > 1:  #if found replace with lcm
                    result.pop()
                    result.pop()
                    result.append(lcm(x,y))
                
                else:
                    break
        return result


        