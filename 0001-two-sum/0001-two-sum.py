class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hasht = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in hasht:
                return (i, hasht[diff]) #storing num and index as pair not index and num : 5:0, 0:5
            hasht[n] = i

        