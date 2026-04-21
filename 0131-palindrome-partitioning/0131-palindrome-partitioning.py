class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Goal: Find all possible palindrome partitions of string s
        # Approach: Backtracking - try all possible splits, keep only palindromic substrings
        # Strategy: At each position, try all possible palindrome substrings starting there
        
        res = []   # Store all valid partitions
        part = []  # Current partition being built
        
        def dfs(i):
            # i: current starting index in string
            
            # Base case: Reached end of string, save current partition
            if i >= len(s):
                res.append(part.copy())  # Must copy
                return
            
            # Try all possible substrings starting at index i
            for j in range(i, len(s)):
                # Check if substring s[i:j+1] is a palindrome
                if isPali(s, i, j):
                    # Valid palindrome - add to current partition
                    part.append(s[i:j+1])
                    
                    # Recursively partition remaining string starting at j+1
                    dfs(j + 1)
                    
                    # Backtrack: remove last added substring
                    part.pop()
        
        def isPali(s, l, r):
            # Helper: Check if substring s[l:r+1] is palindrome
            # Use two pointers from both ends
            
            while l < r:
                # If characters don't match, not a palindrome
                if s[l] != s[r]:
                    return False
                # Move pointers inward
                l, r = l + 1, r - 1  # Fixed typo: was '1,r' should be 'l,r'
            
            # All characters matched, it's a palindrome
            return True
        
        dfs(0) 
        return res  