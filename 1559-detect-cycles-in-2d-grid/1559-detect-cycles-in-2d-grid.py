class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # Goal: Detect if there's a cycle in the grid
        # Rules: Cycle = path of same-letter cells that returns to starting point
        #        Can only move to adjacent cells (up/down/left/right)
        # Approach: DFS from each unvisited cell, detect back edges (visited neighbors)
        
        m, n = len(grid), len(grid[0])
        
        # Track visited cells using 1D array (flatten 2D grid)
        # Index conversion: grid[r][c] → visit[r * n + c]
        visit = [False] * (m * n)
        
        # Four directions: left, right, up, down
        dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))
        
        def dfs(r, c, pr, pc):
            # r, c: current cell position
            # pr, pc: parent cell position (where we came from)
            # Returns: True if cycle detected, False otherwise
            
            # Mark current cell as visited
            visit[r * n + c] = True
            
            # Explore all 4 adjacent cells
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc  # Neighbor coordinates
                
                # Skip parent cell (don't go back immediately)
                if (nr, nc) != (pr, pc):
                    # Check if neighbor is within bounds
                    if 0 <= nr < m and 0 <= nc < n:
                        # Check if neighbor has same letter (required for cycle)
                        if grid[nr][nc] == grid[r][c]:
                            # Cycle detected if:
                            # 1. Neighbor already visited (back edge) OR
                            # 2. DFS from neighbor finds a cycle
                            if visit[nr * n + nc] or dfs(nr, nc, r, c):
                                return True
            
            # No cycle found from this cell
            return False
        
        # Try DFS from every unvisited cell
        # Return True if any starting point finds a cycle
        return any(not visit[i] and dfs(i // n, i % n, -1, -1) for i in range(m * n))