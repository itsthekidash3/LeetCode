class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Goal: Find all unique combinations that sum to target
        # Rules: Each number used at most once, no duplicate combinations
        # Approach: Backtracking with duplicate skipping (sort first)
        
        candidates.sort()  # CRITICAL: Sort to group duplicates together
        res = []
        
        def backtrack(i, cur, total):  # Fixed: was 'backtracking' in call, 'backtrack' in def
            # i: current starting index in candidates
            # cur: current combination being built
            # total: remaining sum needed to reach target
            
            # Base case 1: Found valid combination (sum equals target)
            if total == 0:
                res.append(cur.copy())
                return 
            
            # Base case 2: Exceeded target or out of elements
            if total < 0 or i >= len(candidates):  # Fixed: added i >= len check
                return
            
            # Try each remaining candidate starting from index i
            for j in range(i, len(candidates)):  # Fixed: should be j, not i; start from i
                # Skip duplicates at same decision level
                # If current element equals previous at this level, skip it
                if j > i and candidates[j] == candidates[j - 1]:  # Fixed: compare j with j-1, check j > i
                    continue
                
                # Decision: Include candidates[j]
                cur.append(candidates[j])
                backtrack(j + 1, cur, total - candidates[j])  # Move to next index (each used once)
                
                # Backtrack: Remove last element
                cur.pop()
        
        backtrack(0, [], target)  
        return res  