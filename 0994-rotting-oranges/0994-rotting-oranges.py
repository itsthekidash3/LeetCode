"""
PROBLEM: 994. Rotting Oranges
APPROACH: Multi-source BFS (level-order / layer-by-layer expansion)
TIME COMPLEXITY: O(rows * cols) → every cell is enqueued and processed at most once
SPACE COMPLEXITY: O(rows * cols) → worst case, queue can hold every cell (e.g. all oranges start rotten)

CORE INSIGHT:
Treat every initially rotten orange as a simultaneous BFS source.
Processing the queue one full "layer" (minute) at a time naturally
models rot spreading outward one minute per adjacency step —
so the number of BFS layers == minutes elapsed.
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0

        rows, cols = len(grid), len(grid[0])

        # First pass: scan the whole grid to
        # 1) count all fresh oranges (need to track when they've all rotted)
        # 2) seed the BFS queue with every ALREADY-rotten orange
        # WHY: rot spreads from all rotten oranges at once, not just one —
        # → this is what makes it "multi-source" BFS
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        # BFS expansion, one full minute (layer) at a time.
        # Loop condition: stop early if no fresh oranges remain (fresh == 0)
        # → no need to keep simulating once everything is rotten
        while q and fresh > 0:

            # STEP-BY-STEP TRACE (small example):
            # grid = [[2,1,1],
            #         [1,1,0],
            #         [0,1,1]]
            # Initial q = [[0,0]], fresh = 6
            #
            # Minute 1 (process len(q)==1 cell): pop (0,0)
            #   → rots (0,1) and (1,0) → q = [[0,1],[1,0]], fresh = 4
            # time becomes 1
            #
            # Minute 2 (process len(q)==2 cells): pop (0,1) → rots (1,1)
            #                                      pop (1,0) → rots (1,1) already rotten, skip
            #   → q = [[1,1]], fresh = 3
            # time becomes 2
            # ...continues until fresh == 0 or queue empties

            # KEY TRICK: snapshot len(q) BEFORE the inner loop starts.
            # WHY: q grows as we append newly-rotten oranges during this
            # same minute — freezing the length ensures we only process
            # oranges that were rotten at the START of this minute,
            # → this is what enforces "one layer = one minute"
            for i in range(len(q)):
                r, c = q.popleft()

                # Check all 4 neighbors (up/down/left/right)
                for dr, dc in directions:
                    row, col = dr + r, dc + c

                    # Skip invalid neighbors:
                    # - out of bounds (row/col negative or beyond grid edges)
                    # - not fresh (0 = empty cell, 2 = already rotten)
                    # → only a fresh orange (1) can be newly infected
                    if (row < 0 or row == len(grid) or
                        col < 0 or col == len(grid[0]) or
                        grid[row][col] != 1):
                        continue

                    # Infect this neighbor: mark rotten, enqueue for
                    # next minute's expansion, decrement remaining fresh count
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1

            # One full layer (minute) of BFS has completed
            time += 1

        # Edge case: if fresh > 0 here, some oranges were unreachable
        # → rot could never spread to them, so return -1
        # Edge case: if there were 0 fresh oranges to begin with, the
        # while loop never runs (fresh > 0 is False), time stays 0,
        # and fresh == 0 → correctly returns 0
        return time if fresh == 0 else -1