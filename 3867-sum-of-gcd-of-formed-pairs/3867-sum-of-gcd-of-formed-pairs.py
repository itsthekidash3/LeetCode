from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        """
        Solution approach:
        1. Build prefixGcd array where each element is gcd(nums[i], max_so_far)
        2. Sort the prefixGcd array
        3. Pair smallest with largest elements using two pointers
        4. Sum the GCD of all pairs
        """
        
        n = len(nums)
        
        # Step 1: Construct the prefixGcd array
        prefixGcd = [0] * n  # Initialize array to store prefix GCD values
        mFar = 0  # Track the maximum value seen so far
        
        for i in range(n):
            # Update the running maximum up to index i
            mFar = max(nums[i], mFar)
            
            # prefixGcd[i] = gcd of current element and max element up to index i
            prefixGcd[i] = gcd(mFar, nums[i])
        
        # Step 2: Sort prefixGcd in non-decreasing order
        # This allows us to pair smallest with largest
        prefixGcd.sort()
        
        # Step 3: Form pairs using two-pointer technique
        left, right = 0, n - 1  # Start from both ends
        total = 0  # Accumulator for sum of pair GCDs
        
        # Pair elements from opposite ends until pointers meet
        while left < right:
            # Compute GCD of the paired elements and add to total
            total += gcd(prefixGcd[left], prefixGcd[right])
            left += 1   # Move left pointer inward
            right -= 1  # Move right pointer inward
        
        # If n is odd, middle element remains unpaired (automatically ignored)
        
        return total