class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # STRATEGY: Direct calculation without generating all strings
        # KEY INSIGHT: Happy strings form a tree structure when sorted lexicographically
        # - Position 0: 3 choices (a, b, c)
        # - Position 1 onwards: 2 choices each (any letter except the previous one)
        # Total happy strings of length n = 3 * 2^(n-1)
        
        # Calculate total number of happy strings of length n
        total = 3 * (2 ** (n - 1))
        if k > total:  # Not enough happy strings
            return ""
        
        # Convert to 0-indexed for easier math
        k -= 1
        result = []
        last = ""  # Track the last character to avoid repetition
        
        # Build the string position by position
        for pos in range(n):
            # Calculate how many strings exist under each branch at this position
            # At position i, each choice branches into 2^(n-i-1) strings
            branch = 2 ** (n - pos - 1)
            
            # Get valid choices (exclude the last character used)
            choices = [c for c in "abc" if c != last]
            # At pos 0: choices = ['a', 'b', 'c'] (3 choices)
            # At pos 1+: choices has 2 elements (exclude last char)
            
            # Determine which choice leads to the kth string
            # idx = which branch to take (0, 1, or 2)
            idx = k // branch
            result.append(choices[idx])
            
            # Update for next iteration
            last = choices[idx]  # Remember this char to exclude it next time
            k %= branch  # Update k to be relative to the chosen branch
        
        return "".join(result)