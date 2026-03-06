class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # Check if all '1's form a single contiguous segment (no gaps)
        # Strategy: Look for the pattern "01" which indicates '1's restarting after a '0'
        
        # Iterate through string starting from index 1 (compare each char with previous)
        for i in range(1, len(s)):
            # If we find a '1' that comes right after a '0', that means
            # the '1's are broken into multiple segments (we've seen '1's, then '0's, now '1's again)
            if s[i] == '1' and s[i - 1] == '0': 
                return False
        
        # If we never found the "01" pattern, all '1's must be in one continuous block
        return True