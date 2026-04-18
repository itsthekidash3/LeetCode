class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Goal: Generate all unique subsets from array that may contain duplicates
        # Approach: Backtracking with duplicate skipping
        # Key insight: Sort first, then skip duplicates when excluding elements
        
        res = []
        nums.sort()  # CRITICAL: Sort to group duplicates together
        
        def dfs(i, subset):
            # i: current index in nums
            # subset: current subset being built
            
            # Base case: processed all elements, save current subset
            if i == len(nums):
                res.append(subset.copy())  # Must copy
                return
            
            # Decision 1: INCLUDE nums[i]
            subset.append(nums[i])
            dfs(i + 1, subset)  # Recurse to next element
            
            # Backtrack: remove nums[i] to explore exclude path
            subset.pop()
            
            # Decision 2: EXCLUDE nums[i]
            # Key optimization: Skip all duplicate values
            # If we exclude nums[i], we must also exclude all following duplicates
            # to avoid generating duplicate subsets
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1  # Skip duplicates
            
            dfs(i + 1, subset)  # Recurse with next different element
        
        dfs(0, [])  # Fixed typo: was 'dfes'
        return res  # Fixed typo: was 'result'