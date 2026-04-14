class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Goal: Generate all possible subsets (power set) of nums
        # Approach: Backtracking with decision tree (include/exclude each element)
        # Time: O(2^n * n), Space: O(n) for recursion depth
        
        res = []  # Store all subsets
        subset = []  # Current subset being built 
        
        def dfs(i):
            # i: current index in nums we're deciding on
            
            # Base case: processed all elements, add current subset to results
            if i >= len(nums):
                res.append(subset.copy())  # Must copy, otherwise all point to same list
                return
            
            # Decision 1: INCLUDE nums[i] in current subset
            subset.append(nums[i])
            dfs(i + 1)  # Recurse to next element
            
            # Decision 2: EXCLUDE nums[i] from current subset (backtrack)
            subset.pop()  # Remove nums[i] to explore path without it
            dfs(i + 1)  # Recurse to next element
        
        dfs(0)  # Start from index 0
        return res