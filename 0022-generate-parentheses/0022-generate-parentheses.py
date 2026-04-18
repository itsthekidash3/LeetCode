 # backtracking
        # open and close count
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Goal: Generate all valid combinations of n pairs of parentheses
        # Rules: 
        #   1. Can add '(' if we haven't used all n open parens
        #   2. Can add ')' only if closeN < openN (to keep valid)
        #   3. Valid when openN == closeN == n
        # Approach: Backtracking with constraints
        
        stack = []  # Current parentheses combination being built
        res = []    # Store all valid combinations
        
        def backtrack(openN, closeN):
            # openN: number of '(' used so far
            # closeN: number of ')' used so far
            
            # Base case: Used all n pairs, and they're balanced
            if openN == closeN == n:
                res.append("".join(stack))  # Convert list to string and save
                return
            
            # Decision 1: Add '(' if we haven't used all n open parens
            # Constraint: openN < n (still have open parens available)
            if openN < n:
                stack.append("(")           # Make choice
                backtrack(openN + 1, closeN)  # Explore with this choice
                stack.pop()                 # Backtrack: undo choice
            
            # Decision 2: Add ')' if it keeps parentheses valid
            # Constraint: closeN < openN (ensures we don't add ')' before matching '(')
            if closeN < openN:
                stack.append(")")           # Make choice
                backtrack(openN, closeN + 1)  # Explore with this choice
                stack.pop()                 # Backtrack: undo choice
        
        backtrack(0, 0)  # Start with 0 open and 0 close
        return res