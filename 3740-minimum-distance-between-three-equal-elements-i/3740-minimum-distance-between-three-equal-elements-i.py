from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # Goal: Find minimum distance for valid triplet (i, j, k) where nums[i] == nums[k]
        # Distance formula: 2 * |j - i| + |k - j| where i < j < k
        # Key insight: When nums[i] == nums[k], distance simplifies to 2 * (k - i)
        
        mp = defaultdict(list)  # Map each value to list of its indices
        n = len(nums)
        
        # Step 1: Group indices by their values
        for i in range(n):
            mp[nums[i]].append(i)  # Store index i for value nums[i]
        
        ans = float('inf')  # Initialize with infinity to track minimum
        
        # Step 2: Process each group of indices with same value
        for indices in mp.values():
            # Need at least 3 occurrences to form a valid triplet (i, j, k)
            if len(indices) < 3:
                continue
            
            # Step 3: Try all consecutive triplets of same value
            # Since nums[i] == nums[k], distance = 2 * (k - i)
            # We want to minimize this, so check consecutive triplets
            for i in range(len(indices) - 2):
                # indices[i] = position i, indices[i+2] = position k
                # Any j between them works, distance is same: 2 * (k - i)
                dist = 2 * (indices[i + 2] - indices[i])
                ans = min(ans, dist)
        
        # Return -1 if no valid triplet found, otherwise return minimum distance
        return -1 if ans == float('inf') else ans