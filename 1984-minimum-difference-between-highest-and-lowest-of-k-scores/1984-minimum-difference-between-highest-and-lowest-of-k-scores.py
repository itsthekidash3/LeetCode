class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # no of ways to pick the min and max
        if k == 1:
            return 0 # thats the only number left

        nums.sort() #ascending order
        
        minDiff = float('inf')

        for i in range(len(nums) - k + 1): #4 - 2 + 1 , no of windows possible
            currDiff = nums[i + k -1] - nums[i] # k is the window size 
            minDiff = min(minDiff, currDiff)
        
        return minDiff

        

        