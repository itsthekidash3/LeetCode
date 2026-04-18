class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Goal: Find if word exists in board by moving adjacent cells (up/down/left/right)
        # Rules: Can't reuse same cell in a single path
        # Approach: DFS + Backtracking from every cell as potential starting point
        # add and remove for backtracking
        
        ROWS, COLS = len(board), len(board[0])  # Fixed: was 'rows, cols'
        
        # Track visited cells in current path (prevents reusing same cell)
        path = set()
        
        def dfs(r, c, i):
            # r, c: current position in board
            # i: current index in word we're trying to match
            
            # Base case: Successfully matched entire word
            if i == len(word):
                return True
            
            # Base cases for invalid paths:
            # 1. Out of bounds (r < 0 or c < 0 or r >= ROWS or c >= COLS)
            # 2. Character doesn't match (word[i] != board[r][c])
            # 3. Already visited this cell in current path ((r,c) in path)
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False
            
            # Current cell matches word[i] and is unvisited
            # Mark this cell as visited in current path
            path.add((r, c))
            
            # Explore all 4 directions (down, right, up, left)
            # If ANY direction successfully finds remaining word, return True
            res = (dfs(r + 1, c, i + 1) or  # Down
                   dfs(r, c + 1, i + 1) or  # Right
                   dfs(r - 1, c, i + 1) or  # Up
                   dfs(r, c - 1, i + 1))    # Left
            
            # Backtrack: Remove current cell from path
            # This allows other paths to use this cell
            path.remove((r, c))
            
            return res
        
        # Try starting DFS from every cell in the board
        # Loop through all possible starting positions
        for r in range(ROWS):  # For each row
            for c in range(COLS):  # For each column
                # If word found starting from (r, c), return immediately
                if dfs(r, c, 0):  # Start with index 0 of word
                    return True
        
        # Word not found from any starting position
        return False  # Fixed typo: was 'Falses'