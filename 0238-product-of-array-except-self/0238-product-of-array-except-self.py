class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n
        
        # First pass: calculate the products of all elements to the left of each element
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]  #update the left product
        
        # Second pass: calculate the products of all elements to the right of each element
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]  #update the right product
        
        return result