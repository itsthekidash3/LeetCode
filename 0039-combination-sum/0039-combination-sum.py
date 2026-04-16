class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Goal: Find all unique combinations of candidates that sum to target
        # Rules: Same number can be used unlimited times, combinations must be unique
        # Approach: Backtracking decision tree - at each index, include or exclude
        
        res = []  # Store all valid combinations
        
        def dfs(i, cur, total):
            # i: current index in candidates we're deciding on
            # cur: current combination being built
            # total: sum of numbers in current combination
            
            # Base case 1: Found valid combination (sum equals target)
            if total == target:
                res.append(cur.copy())  # Must copy - cur is modified later
                return
            
            # Base case 2: Invalid path (out of bounds or exceeded target)
            if i >= len(candidates) or total > target:  
                return
            
            # Decision 1: INCLUDE candidates[i] (can reuse same number)
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])  # Stay at index i (allow reuse)
            
            # Decision 2: EXCLUDE candidates[i] (backtrack and move to next)
            cur.pop()  # Remove last added element (backtracking step)
            dfs(i + 1, cur, total)  # Move to next index
        
        dfs(0, [], 0)  # Start: index 0, empty combination, sum 0
        return res