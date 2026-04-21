class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Goal: Generate all possible letter combinations from phone digit mapping
        # Approach: Backtracking - for each digit, try all its possible letters
        # Build combinations character by character
        
        # Edge case: empty input
        if not digits:
            return []
        
        res = []  # Store all valid combinations
        
        # Phone keypad mapping (like old flip phones)
        digitToChar = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        def backtrack(i, curStr):  # Fixed: was 'dfs', call was 'backtrack'
            # i: current index in digits string
            # curStr: current combination being built
            
            # Base case: Built complete combination (length matches input)
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            # Try each letter mapped to current digit
            for c in digitToChar[digits[i]]:
                # Recurse with next digit and extended string
                backtrack(i + 1, curStr + c)  # Fixed typo: 'C' → 'c'
        
        backtrack(0, "")  # Start with index 0 and empty string
        return res