class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum2 =  {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in sum2:
                return (sum2[diff],i)
            sum2[num] = i #storing each num in dict with index value
