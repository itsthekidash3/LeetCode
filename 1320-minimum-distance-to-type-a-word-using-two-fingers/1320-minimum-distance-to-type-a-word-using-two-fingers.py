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


    # ========== SPACE-OPTIMIZED APPROACH (2D DP) ==========
    # def minimumDistance(self, word):
    #     # Goal: Same problem, but optimize space from O(n × 26 × 26) to O(26)
    #     # Key insight: Only need previous state, not entire history
    #     # Track one "free" finger position in dp[j], other finger just typed previous char
    #     
    #     n = len(word)
    #     dp = [0] * 26   # dp[j] = min cost with free finger at position j
    #     ndp = [0] * 26  # Next state buffer
    #     
    #     # Process transitions character by character
    #     for i in range(1, n):
    #         p = ord(word[i - 1]) - ord('A')  # Previous character (just typed)
    #         t = ord(word[i]) - ord('A')      # Current target character
    #         
    #         # Option 1: Use finger that just typed p to type t
    #         # Free finger stays at position j
    #         for j in range(26):
    #             ndp[j] = dp[j] + self.cal(p, t)
    #         
    #         # Option 2: Use free finger at j to type t
    #         # Finger that typed p becomes the new free finger
    #         for j in range(26):
    #             ndp[p] = min(ndp[p], dp[j] + self.cal(j, t))
    #         
    #         # Swap buffers (ndp becomes current state)
    #         dp, ndp = ndp, dp
    #     
    #     return min(dp)  # Minimum across all free finger positions