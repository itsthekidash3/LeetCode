class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        #minimum of the maximum pair sum
        N = len(nums)
        nums.sort() # last + first element
        res = -1

        for i in range( N // 2):
            res = max(res, (nums[i] + nums[N - i - 1]))
        
        return res