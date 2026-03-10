class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j][last] = number of stable arrays with i zeros and j ones, where:
        # last=0 means the array ends with 0, last=1 means it ends with 1
        # A "stable array" means no more than 'limit' consecutive same digits
        dp = [[[0,0] for _ in range(one+1)] for _ in range(zero+1)]
        
        # Base case: arrays with only zeros (length 1 to limit)
        # We can place 1,2,...,limit consecutive zeros at the start
        for i in range(1, min(zero,limit)+1):
            dp[i][0][0] = 1
        
        # Base case: arrays with only ones (length 1 to limit)
        # We can place 1,2,...,limit consecutive ones at the start
        for j in range(1, min(one,limit)+1):
            dp[0][j][1] = 1
        
        # Fill the DP table
        for i in range(1, zero+1):
            for j in range(1, one+1):
                
                # over0 = count of arrays we need to SUBTRACT where we'd have
                # (limit+1) consecutive zeros ending at position (i,j)
                # This happens when we had 'limit' zeros already, then the previous
                # digit was a 1, and we're adding one more 0
                over0 = dp[i-limit-1][j][1] if i-limit >= 1 else 0
                
                # over1 = count of arrays we need to SUBTRACT where we'd have
                # (limit+1) consecutive ones ending at position (i,j)
                over1 = dp[i][j-limit-1][0] if j-limit >= 1 else 0
                
                # To end with 0: take all arrays with (i-1) zeros and add a 0
                # But subtract cases where this creates (limit+1) consecutive zeros
                dp[i][j][0] = (
                    dp[i-1][j][0] + dp[i-1][j][1] - over0
                ) % MOD
                
                # To end with 1: take all arrays with (j-1) ones and add a 1
                # But subtract cases where this creates (limit+1) consecutive ones
                dp[i][j][1] = (
                    dp[i][j-1][0] + dp[i][j-1][1] - over1
                ) % MOD
        
        # Sum arrays ending in 0 and arrays ending in 1
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD