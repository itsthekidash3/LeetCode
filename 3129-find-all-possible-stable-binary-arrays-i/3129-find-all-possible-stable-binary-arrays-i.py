class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # dp[z][o][last] = number of ways to build a stable array using z zeros and o ones,
        # where last indicates what the most recent consecutive group was (0 for zeros, 1 for ones)
        dp = [[[-1]*2 for _ in range(201)] for _ in range(201)]
        
        def solve(z, o, last):
            # Base case: if we've used exactly 'zero' zeros and 'one' ones, we found a valid array
            if z == zero and o == one:
                return 1
            
            # Return cached result if already computed
            if dp[z][o][last] != -1:
                return dp[z][o][last]
            
            res = 0
            
            # If the last group was zeros, we must now add a group of ones
            if last == 0:
                # Try adding k consecutive ones (where 1 <= k <= limit)
                for k in range(1, limit + 1):
                    if o + k > one: break  # Can't exceed our target count
                    res = (res + solve(z, o + k, 1)) % MOD
            else:
                # If the last group was ones, we must now add a group of zeros
                # Try adding k consecutive zeros (where 1 <= k <= limit)
                for k in range(1, limit + 1):
                    if z + k > zero: break  # Can't exceed our target count
                    res = (res + solve(z + k, o, 0)) % MOD
            
            # Cache and return result
            dp[z][o][last] = res
            return res
        
        res = 0
        
        # Start by placing an initial group of k zeros (1 <= k <= min(limit, zero))
        for k in range(1, min(limit, zero) + 1):
            res = (res + solve(k, 0, 0)) % MOD
        
        # OR start by placing an initial group of k ones (1 <= k <= min(limit, one))
        for k in range(1, min(limit, one) + 1):
            res = (res + solve(0, k, 1)) % MOD
        
        return res