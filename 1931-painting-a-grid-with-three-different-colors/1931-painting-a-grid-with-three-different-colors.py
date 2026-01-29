class Solution:
    def colorTheGrid(self, R: int, C: int) -> int:

        MOD = 10 ** 9 + 7

        #get the last "R" colours

        def get(mask):
            arr = []
            for _ in range(R):
                arr.append(mask % 3)
                mask //=3
            return arr 
        
        def conv(arr):
            mask = 0
            for x in arr[::-1]:
                mask *= 3
                mask += x
            return mask
        

        @cache

        # x -> 0 to R-1
        # y -> 0 to C-1

        def count(mask, x ,y):
            if x == R:
                return count(mask, 0 ,y + 1)
            if y == C:
                return 1
            
            total = 0
            arr = get(mask)  #getting the last r colors while filling

            # we want to check the previous column

            if x - 1 >= 0:
                color_above = arr[0]  # first element of the array
            else:
                color_above = -1
            
            if y - 1 >= 0:
                color_left = arr[-1] # last element of the arr
            else:
                color_left = -1
            


            for c in range(3):
                if c != color_above and c != color_left:
                    new_arr = [c] + arr[:-1] # lose the most significant bit or last color
                    total += count(conv(new_arr), x+1, y)
            
            return total % MOD
        
        return count(0,0,0) % MOD
        