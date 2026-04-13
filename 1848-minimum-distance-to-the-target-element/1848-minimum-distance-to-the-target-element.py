class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        # Goal: Find minimum distance from start  to any occurrence of target value
        # Distance = |index - start|
        # Approach: Find all indices containing target, compute min distance value
        
        # Step 1: Find all indices where nums[i] == target
        indices = [i for i, x in enumerate(nums) if x == target]  
        
        # Step 2: Sort indices (optimization: enables binary search, though not used here)
        # Note: enumerate returns indices in order, so sorting is redundant
        indices.sort()
        
        # Step 3: Find minimum distance from start to any target index
        val = float('inf')  
        for i in range(len(indices)):
            # Calculate absolute distance from current target index to start
            val = min(val, abs(indices[i] - start))
        
        return val


    # ========== OPTIMIZED SINGLE-PASS APPROACH ==========
    # def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
    #     # Goal: Find min distance in one pass without storing all indices
    #     # Approach: Track minimum distance while iterating through array
    #     
    #     min_dist = float('inf')
    #     
    #     for i, x in enumerate(nums):
    #         if x == target:
    #             # Update minimum distance whenever we find target
    #             min_dist = min(min_dist, abs(i - start))
    #     
    #     return min_dist