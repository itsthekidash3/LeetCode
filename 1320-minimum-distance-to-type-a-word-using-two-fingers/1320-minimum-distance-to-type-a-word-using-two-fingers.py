class Solution:
    def cal(self, a, b):
        # Helper: Calculate Manhattan distance between two letters on keyboard
        # Keyboard is 6 columns wide (A-F, G-L, M-R, S-X, Y-Z with padding)
        # Distance = |row_diff| + |col_diff|
        return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

    def minimumDistance(self, word: str) -> int:
        # Goal: Type word with two fingers, minimizing total movement distance
        # Rules: Start with fingers anywhere, move one finger at a time to type each letter
        # Approach: 3D DP tracking positions of both fingers after typing prefix of word
        
        # dp[i][j][k] = min cost to type first i characters with:
        #   - finger 1 at letter j (0-25 for A-Z)
        #   - finger 2 at letter k (0-25 for A-Z)
        
        n = len(word)
        
        # Initialize DP table: (n+1) states × 26 × 26 positions
        dp = [[[0] * 26 for _ in range(26)] for _ in range(n + 1)]
        
        # Process each character in word
        for i in range(n):
            t = ord(word[i]) - ord('A')  # Current target letter (0-25)
            
            # Step 1: Initialize next state with infinity (will take minimum)
            for j in range(26):
                for k in range(26):
                    dp[i + 1][j][k] = 1000000
            
            # Step 2: Try all current finger positions and decide which finger to move
            for j in range(26):  # Finger 1 position before typing word[i]
                for k in range(26):  # Finger 2 position before typing word[i]
                    # Option 1: Move finger 2 to type word[i], finger 1 stays at j
                    dp[i + 1][j][t] = min(dp[i + 1][j][t], 
                                          dp[i][j][k] + self.cal(k, t))
                    
                    # Option 2: Move finger 1 to type word[i], finger 2 stays at k
                    dp[i + 1][t][k] = min(dp[i + 1][t][k], 
                                          dp[i][j][k] + self.cal(j, t))
        
        # Step 3: Find minimum cost across all final finger positions
        ans = 100000
        for j in range(26):
            for k in range(26):
                ans = min(ans, dp[n][j][k])
        
        return ans