class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        nums.sort()

        for i,a in enumerate(nums):
            if  i > 0 and a == nums[i-1]: 
                continue # this is not the first value in input array and it is equal to the previous number
            l,r = i+1, len(nums) - 1 # two pointers
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0: #value greater that expected, decrease the number i.e right pointer
                    r -= 1
                elif threeSum < 0:#value less that expected, decrease the number i.e right pointer
                    l += 1
                else:
                    arr.append([a,nums[l], nums[r]])
                    l += 1 #update any one pointer after appending to arr
                            #the conditions will handle the other pointer
                    while nums[l] == nums[l-1] and l<r: #we dont want the same value
                        l += 1
        return arr