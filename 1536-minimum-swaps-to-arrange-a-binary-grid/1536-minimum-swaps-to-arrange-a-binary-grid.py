class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        # APPROACH: Greedy + Bubble Sort intuition
        # - For the grid to be valid (upper triangle of 1s), row i must have
        #   all its trailing 1s end BEFORE column i (i.e. last 1 in row i must be at index <= i-1... wait:
        #   actually row i needs (N-1-i) zeros on the RIGHT side
        # - So track the LAST position of 1 in each row → that tells us how many trailing zeros we have
        # - For row i, we need a row whose last 1 is at index <= i (so N-1-i trailing zeros)
        # - Greedily find the closest such row below, bubble it up counting swaps
        # - If no valid row exists → return -1

        N = len(grid)

        # find the index of the last 1 in each row (farthest right 1)
        rows = []
        for i in range(N):
            farthest = -1
            for j in range(N):
                if grid[i][j] == 1:
                    farthest = j  # track rightmost 1 in this row
            rows.append(farthest)  # Bug fix: was rows.append[j] → should be rows.append(farthest)

        count = 0

        for i in range(N):
            # row i needs its last 1 to be at column <= i (enough trailing zeros)
            found = False
            for j in range(i, N):  # Bug fix: search from i onwards, not from 0
                if rows[j] <= i:   # this row has enough trailing zeros
                    # bubble row j up to position i, each step is one swap
                    rows = rows[:i] + [rows[j]] + rows[i:j] + rows[j+1:]  # Bug fix: proper bubble up
                    count += j - i  # number of swaps = distance to bubble up
                    found = True
                    break

            if not found:  # Bug fix: -1 check was in wrong place
                return -1

        return count