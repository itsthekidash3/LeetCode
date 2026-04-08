class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        # Goal: Apply multiplication queries to array, then return XOR of all elements
        # Each query: multiply elements at indices [l, r] with step k by value v
        # Final result: XOR of all modified elements
        
        MOD = 10 ** 9 + 7
        
        # Step 1: Process each query
        for l, r, k, v in queries:
            # l: start index (inclusive)
            # r: end index (inclusive)
            # k: step size (increment)
            # v: multiplier value
            
            # Multiply elements at indices l, l+k, l+2k, ... up to r
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % MOD  # Apply modulo to prevent overflow
        
        # Step 2: Calculate XOR of all elements in modified array
        s = 0  # XOR identity element (0 XOR x = x)
        for x in nums:
            s ^= x  # XOR current element with running result
        
        return s