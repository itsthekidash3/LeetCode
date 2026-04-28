class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Goal: Find the maximum area of an island (connected 1's)
        # Approach: DFS from each unvisited land cell, count connected cells
        # Return the largest island size found
        
        # Get grid dimensions
        rows, cols = len(grid), len(grid[0])  
        
        # Track visited cells to avoid counting same cell multiple times
        visit = set()
        
        def dfs(r, c):
            # Base cases - return 0 (no area) if:
            # 1. Out of bounds (r < 0 or r >= rows or c < 0 or c >= cols)
            # 2. Water cell (grid[r][c] == 0)
            # 3. Already visited ((r,c) in visit)
            if (r < 0 or r == rows or c < 0 or c == cols or 
                grid[r][c] == 0 or (r, c) in visit):
                return 0
            
            # Mark current cell as visited
            visit.add((r, c))
            
            # Return area: 1 (current cell) + area from all 4 directions
            return (1 + dfs(r + 1, c) +  # Down
                        dfs(r - 1, c) +  # Up
                        dfs(r, c + 1) +  # Right
                        dfs(r, c - 1))   # Left
        
        area = 0  # Track maximum island area found
        
        # Scan entire grid, try DFS from every cell
        for r in range(rows):
            for c in range(cols):
                # Update max area with result from this cell
                # dfs returns 0 for water/visited cells, or island size for new land
                area = max(area, dfs(r, c))
        
        return area