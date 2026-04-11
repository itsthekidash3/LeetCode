# borrowed code from Aarzo for better understanding

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        # Goal: Efficiently apply multiplication queries then compute XOR of all elements
        # Optimization: Split queries into "large k" (brute force) and "small k" (batch processing)
        # Threshold: sqrt(n) - balances brute force cost vs batch processing overhead
        
        MOD = 10**9 + 7
        n = len(nums)
        limit = int(n ** 0.5) + 1  # sqrt(n) threshold for query classification
        
        def mod_pow(base, exp):
            # Fast exponentiation: compute (base^exp) % MOD in O(log exp) time
            result = 1
            
            while exp > 0:
                if exp & 1:  # If exp is odd, multiply result by base
                    result = (result * base) % MOD
                
                base = (base * base) % MOD  # Square the base
                exp >>= 1  # Divide exp by 2 (right shift)
            
            return result
        
        def mod_inverse(x):
            # Compute modular inverse using Fermat's Little Theorem
            # For prime MOD: x^(-1) ≡ x^(MOD-2) (mod MOD)
            return mod_pow(x, MOD - 2)
        
        small_queries = {}  # Group queries by step size k
        
        # Step 1: Process queries based on step size
        for l, r, k, v in queries:
            if k >= limit:
                # Large k: Few elements affected, process immediately (brute force)
                i = l
                while i <= r:
                    nums[i] = (nums[i] * v) % MOD
                    i += k
            else:
                # Small k: Many elements affected, batch for efficient processing
                if k not in small_queries:
                    small_queries[k] = []
                
                small_queries[k].append((l, r, v))
        
        # Step 2: Batch process small k queries using difference array technique
        for k, group in small_queries.items():
            diff = [1] * n  # Difference array: stores cumulative multipliers
            
            # Build difference array for all queries with same k
            for l, r, v in group:
                # Mark start of range: multiply by v
                diff[l] = (diff[l] * v) % MOD
                
                # Mark end of range: divide by v (undo multiplication after range)
                steps = (r - l) // k  # Number of steps from l to r with step k
                next_pos = l + (steps + 1) * k  # First index after range
                
                if next_pos < n:
                    # Use modular inverse to "undo" multiplication
                    diff[next_pos] = (diff[next_pos] * mod_inverse(v)) % MOD
            
            # Apply difference array using prefix product at intervals of k
            for i in range(n):
                if i >= k:
                    # Propagate multiplier from position i-k to i
                    diff[i] = (diff[i] * diff[i - k]) % MOD
                
                # Apply cumulative multiplier to actual array
                nums[i] = (nums[i] * diff[i]) % MOD
        
        # Step 3: Compute XOR of all modified elements
        answer = 0
        for num in nums:
            answer ^= num
        
        return answer