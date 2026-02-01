class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # min1 will store the smallest value seen so far (excluding nums[0])
        # min2 will store the second smallest value seen so far
        min1 = float('inf')
        min2 = float('inf')
        
        # Iterate over the array starting from index 1
        # (nums[0] is handled separately at the end)
        for x in nums[1:]:
            # If current value is smaller than the smallest so far:
            # shift the old min1 to min2, and update min1
            if x < min1:
                min2 = min1
                min1 = x
            # Otherwise, if x is between min1 and min2,
            # update only min2
            elif x < min2:
                min2 = x
        
        # Final cost is nums[0] + the two smallest values
        # found in the rest of the array
        return nums[0] + min1 + min2
