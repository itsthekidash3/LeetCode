class Solution:
    def numSteps(self, s: str) -> int:

        # bit manipulation
        #if even divide by 2 -> right shift
        # if odd add 1 - OR the number
        # no of steps 
        # the binary number is a string. 
        # convert to a binarty number

        # check with and 1, that gives 1 or zero

        # if len(s) = 1 return the steps only if 1 else add one and return steps + 1

        steps = 0
        num = int(s,2)
        while num != 1 :
            steps += 1
            if num & 1 == 0: #if its a number divisbile by 2
                num //= 2
            elif num & 1 == 1 : # if its odd
                num += 1
        
        return steps

            

        



        