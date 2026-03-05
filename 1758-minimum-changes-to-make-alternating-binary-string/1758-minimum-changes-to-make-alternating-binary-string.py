class Solution:
    def minOperations(self, s: str) -> int:
        """
        Problem: Find minimum operations to make a binary string alternate between 0 and 1.
        
        Approach: There are only 2 possible alternating patterns - starting with 0 (0,1,0,1...) 
        or starting with 1 (1,0,1,0...). Count mismatches for each pattern and return the minimum.
        """
        
        N = len(s)
        best = N  # worst case: change every character
        
        # Try both possible alternating patterns
        for start in [0, 1]:
            count = 0
            for i in range(N):
                # Calculate what the character should be at position i
                # If start=0: positions 0,2,4... should be 0, positions 1,3,5... should be 1
                # If start=1: positions 0,2,4... should be 1, positions 1,3,5... should be 0
                # (start + i) % 2 gives us the expected digit for this position
                
                if int(s[i]) != (start + i) % 2:
                    count += 1  # Increment count if current character doesn't match the pattern
            
            # Keep track of the pattern that requires fewer changes
            best = min(best, count)
        
        return best