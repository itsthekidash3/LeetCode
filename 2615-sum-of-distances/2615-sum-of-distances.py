# borrowed code from vikram

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # Goal: For each index i, calculate sum of absolute distances to all indices with same value
        # Example: nums=[1,3,1,1,2], for i=0 (value=1), distance to i=2,4 → |0-2| + |0-4| = 6
        # Approach: Group indices by value, use prefix sum math to avoid O(n²) comparisons
        
        n = len(nums)
        ans = [0] * n  # Store result distances
        
        # Step 1: Group indices by their values
        mp = defaultdict(list)  # value → list of indices with that value
        
        for i, v in enumerate(nums):
            mp[v].append(i)  # mp[1] = [0, 2, 3], mp[3] = [1], mp[2] = [4]
        
        # Step 2: For each group of same-value indices, calculate distances
        for pos in mp.values():
            # pos = list of indices with same value, e.g., [0, 2, 3] for value=1
            
            total = sum(pos)  # Sum of all indices in this group
            left_sum = 0  # Running sum of indices to the left of current
            m = len(pos)  # Number of indices with this value
            
            # Process each index in the group
            for i in range(m):
                # Split into left and right portions relative to pos[i]
                
                # right_sum = sum of all indices to the right of pos[i]
                right_sum = total - left_sum - pos[i]
                
                # Calculate distance to all left indices
                # pos[i] appears i times on left, each at distance (pos[i] - left_index)
                # Sum of (pos[i] - left_index) for all left = pos[i]*i - left_sum
                left = pos[i] * i - left_sum
                
                # Calculate distance to all right indices
                # (m - i - 1) indices on right, each at distance (right_index - pos[i])
                # Sum of (right_index - pos[i]) for all right = right_sum - pos[i]*(m-i-1)
                right = right_sum - pos[i] * (m - i - 1)
                
                # Total distance = distance to left + distance to right
                ans[pos[i]] = left + right
                
                # Update left_sum for next iteration
                left_sum += pos[i]
        
        return ans