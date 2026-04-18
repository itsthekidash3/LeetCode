class Solution:
    def mirrorDistance(self, n: int) -> int:
        # Goal: Find absolute difference between n and its digit reversal
        # Approach 1: String manipulation (simple and readable)
        
        # Convert number to string for easy reversal
        num = str(n)
        
        # Reverse the string using slice notation [::-1]
        numR = num[::-1]
        
        # Convert reversed string back to integer and find absolute difference
        return abs(n - int(numR))


    # ========== APPROACH 2: MATHEMATICAL REVERSAL (NO STRING CONVERSION) ==========
    # def mirrorDistance(self, n: int) -> int:
    #     # Goal: Reverse digits mathematically without string conversion
    #     # Approach: Extract digits one by one using modulo and division
    #     
    #     rev = 0  # Store reversed number
    #     x = n    # Working copy of n
    #     
    #     # Build reversed number digit by digit
    #     while x > 0:
    #         # divmod(x, 10) returns (quotient, remainder)
    #         # quotient = x // 10 (remaining digits)
    #         # remainder = x % 10 (current last digit)
    #         x, r = divmod(x, 10)
    #         
    #         # Shift reversed number left and add current digit
    #         # Example: rev=12, r=3 → rev = 12*10 + 3 = 123
    #         rev = 10 * rev + r
    #     
    #     return abs(rev - n)