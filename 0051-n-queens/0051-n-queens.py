class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Goal: Place n queens on n×n chessboard such that no two queens attack each other
        # Rules: Queens attack same row, column, or diagonal
        # Approach: Backtracking - place queen row by row, track attacked positions
        # Optimization: Track columns and diagonals using sets for O(1) lookup
        
        # Track attacked positions (can't place queens here)
        col = set()      # Columns occupied by queens
        posDiag = set()  # Positive diagonals (/) occupied - constant (r+c)
        negDiag = set()  # Negative diagonals (\) occupied - constant (r-c)
        
        res = []  # Store all valid board configurations
        
        # Initialize empty board with all dots
        # board[r][c] = "." means empty, "Q" means queen
        board = [["."] * n for i in range(n)]
        
        def backtrack(r):
            # r: current row we're trying to place a queen in
            
            # Base case: Placed queens in all n rows successfully
            if r == n:
                # Convert board to required format (list of strings)
                # Each row is a string: "...Q.." etc.
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            # Try placing queen in each column of current row
            for c in range(n):
                # Check if position (r, c) is under attack
                # Skip if:
                # 1. Column c is occupied
                # 2. Positive diagonal (r+c) is occupied
                # 3. Negative diagonal (r-c) is occupied
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue  # Can't place queen here, try next column
                
                # Position is safe - place queen and mark attacked positions
                col.add(c)           # Mark column as occupied
                posDiag.add(r + c)   # Mark positive diagonal as occupied
                negDiag.add(r - c)   # Mark negative diagonal as occupied
                board[r][c] = "Q"    # Place queen on board
                
                # Recursively try to place queens in remaining rows
                backtrack(r + 1)
                
                # Backtrack: Remove queen and unmark attacked positions
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."    # Remove queen from board
        
        backtrack(0)  # Start placing queens from row 0
        return res