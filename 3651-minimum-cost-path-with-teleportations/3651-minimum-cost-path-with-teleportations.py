from heapq import heappush, heappop
from bisect import bisect_right
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        """
        Grid shortest path with teleportation.

        - You can move right or down normally (pay grid cost).
        - You can teleport at most k times.
        - A teleport lets you jump to any cell whose value
          is <= current cell's value (sorted by value).
        """

        m, n = len(grid), len(grid[0])

        # dist[pos][t] = minimum cost to reach position `pos`
        # using exactly `t` teleportations
        dist = [[float("inf")] * (k + 1) for _ in range(m * n)]

        # Starting cell can be reached with cost 0 for any teleport count
        for t in range(k + 1):
            dist[0][t] = 0

        # Min-heap: (cost_so_far, teleports_used, row, col)
        pq = [(0, 0, 0, 0)]

        # Sort all cells by grid value (used for teleport logic)
        arr = sorted(
            (grid[i][j], i, j)
            for i in range(m)
            for j in range(n)
        )

        # used[t] = how many cells in `arr` have already been
        # processed for teleport count t
        used = [0] * (k + 1)

        while pq:
            cost, t, i, j = heappop(pq)
            idx = i * n + j

            # If destination is reached, return minimum cost
            if i == m - 1 and j == n - 1:
                return cost

            # Skip outdated states
            if cost > dist[idx][t]:
                continue

            # Move DOWN
            if i + 1 < m:
                new_cost = cost + grid[i + 1][j]
                next_idx = (i + 1) * n + j
                if new_cost < dist[next_idx][t]:
                    dist[next_idx][t] = new_cost
                    heappush(pq, (new_cost, t, i + 1, j))

            # Move RIGHT
            if j + 1 < n:
                new_cost = cost + grid[i][j + 1]
                next_idx = i * n + (j + 1)
                if new_cost < dist[next_idx][t]:
                    dist[next_idx][t] = new_cost
                    heappush(pq, (new_cost, t, i, j + 1))

            # TELEPORT
            if t + 1 <= k:
                # Find all cells with value <= current cell
                limit = bisect_right(arr, grid[i][j], key=lambda x: x[0])

                # Process only unvisited teleport targets
                while used[t] < limit:
                    _, r, c = arr[used[t]]
                    target_idx = r * n + c

                    # Teleport has ZERO cost
                    if cost < dist[target_idx][t + 1]:
                        # Optimization:
                        # If reachable with t+1 teleports,
                        # it's also reachable with any larger teleport count
                        for nt in range(t + 1, k + 1):
                            dist[target_idx][nt] = cost

                        heappush(pq, (cost, t + 1, r, c))

                    used[t] += 1

        return -1
