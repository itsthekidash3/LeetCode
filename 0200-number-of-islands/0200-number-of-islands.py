import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Goal: Count number of islands (connected components of '1's)
        # Approach: BFS from each unvisited land cell, mark all connected cells
        # Each BFS traversal finds one complete island
        
        # Edge case: empty grid
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()  # Track visited cells
        islands = 0    # Count of islands found
        
        def bfs(r, c):
            # BFS to explore entire island starting from (r, c)
            q = collections.deque()
            visit.add((r, c))  
            q.append((r, c))
            
            # Process all cells in current island
            while q:
                row, col = q.popleft()  
                
                # Four directions: down, up, right, left
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions: 
                    r, c = row + dr, col + dc  # Calculate neighbor coordinates
                    
                    # Check if neighbor is valid land cell and unvisited
                    if (r in range(rows) and 
                        c in range(cols) and 
                        grid[r][c] == "1" and 
                        (r, c) not in visit):
                        
                        q.append((r, c))
                        visit.add((r, c))  
        
        # Scan entire grid for unvisited land cells
        for r in range(rows):
            for c in range(cols):
                # Found new island: unvisited land cell
                if grid[r][c] == "1" and (r, c) not in visit: 
                    bfs(r, c)     # Explore entire island
                    islands += 1  # Increment island count
        
        return islands