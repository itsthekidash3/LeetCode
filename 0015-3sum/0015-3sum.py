class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        nums.sort()

        for tar,val in enumerate(nums):
            if  tar > 0 and val == nums[tar-1]: 
                continue # this is not the first value in input array and it is equal to the previous number 
                         #we don’t start a new triplet with the same a twice.
            left,right = tar+1, len(nums) - 1 # two pointers
            while left < right:
                target = val + nums[left] + nums[right]
                if target > 0: #value greater that expected, decrease the number i.e right pointer
                    right -= 1
                elif target < 0:#value less that expected, decrease the number i.e right pointer
                    left += 1
                else:
                    arr.append([val,nums[left], nums[right]])
                    left += 1 #update any one pointer after appending to arr
                            #the conditions will handle the other pointer
                    while nums[left] == nums[left-1] and left<right: #we dont want the same value
                                                                # This check removes duplicate second elements in inner loop
                        left += 1
        return arr