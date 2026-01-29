from collections import defaultdict

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        """
        dp[i][j] = minimum cost to reach cell (i, j)
        Grid cost is paid when entering a cell.
        Teleportation allows zero-cost moves to cells with value <= current.
        """
        m, n = len(grid), len(grid[0])

        # Group all cells by their grid value
        # d[value] = list of (i, j) cells having that value
        d = defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[grid[i][j]].append((i, j))

        inf = float('inf')

        # dp table stores min cost to reach each cell
        dp = [[inf] * n for _ in range(m)]
        dp[0][0] = 0  # starting cell has zero cost

        #  (right and down moves only)
        def update():
            for i in range(m):
                for j in range(n):
                    cost = grid[i][j] + min(
                        dp[i-1][j] if i > 0 else inf,
                        dp[i][j-1] if j > 0 else inf
                    )
                    if cost < dp[i][j]:
                        dp[i][j] = cost

        # Initial DP when no teleport is used
        update()

        # Process teleportation up to k times
        # Teleportation allows all cells with value <= current value
        # to share the minimum dp among them (zero-cost transitions)
        keys = sorted(d, reverse=True)  # process higher values first
        for _ in range(k): #no of teleportation allowed
            dist = inf
            for key in keys:
                # Find the minimum dp among cells with this value
                for i, j in d[key]:
                    if dp[i][j] < dist:
                        dist = dp[i][j]

                # Apply teleport: set all these cells to the same min cost
                for i, j in d[key]:
                    dp[i][j] = dist # travel freely if you can reach i,j with min cost, then you can reach all the cells that used to share the same cost with i,j with this min cost.

            # After teleporting, re-run grid DP to propagate costs
            update()

        # Answer is min cost to reach bottom-right cell
        return dp[-1][-1]
