class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #backtracking with recursion
        # bottom up recursion
        # go down by breaking in to smaller subtrees
        # pop and then append back after visitinf the node, recursively to the result and add them up

        result = [] # base

        # base case
        if len(nums) == 1:
            return [nums.copy()] # return list of list

        for i in range(len(nums)):
            n = nums.pop(0) # pop the first index element
            perms = self.permute(nums) # calling with remaining elements

            for perm in perms:
                perm.append(n) # append n to the result of the perms which we did by removing the element in the first index
            result.extend(perms) # adding multiple values to the result list
            nums.append(n) # add back the n to repeat the same process
        
        return result







        