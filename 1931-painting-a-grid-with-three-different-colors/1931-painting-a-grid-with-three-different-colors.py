class Solution:
    def colorTheGrid(self, R: int, C: int) -> int:

        MOD = 10 ** 9 + 7

        # ----------------------------------------------------
        # mask represents the last R colors used (base-3 number)
        # Each digit = color of a cell
        # Least significant digit = most recently placed cell
        # ----------------------------------------------------

        # Convert mask -> array of last R colors
        def get(mask):
            arr = []
            for _ in range(R):
                arr.append(mask % 3)   # extract base-3 digit
                mask //= 3
            return arr                 # arr[0] = color of cell above

        # Convert array of colors back -> mask (base-3)
        def conv(arr):
            mask = 0
            for x in arr[::-1]:        # most significant first
                mask = mask * 3 + x
            return mask

        @cache
        # mask : last R placed colors
        # x    : current row (0..R-1)
        # y    : current column (0..C-1)
        def count(mask, x, y):

            # Finished one column → move to next column
            if x == R:
                return count(mask, 0, y + 1)

            # Finished all columns → valid coloring
            if y == C:
                return 1

            total = 0
            arr = get(mask)  # current state of last R colors

            # ----------------------------
            # Constraints
            # ----------------------------

            # Color of the cell directly above (same column)
            if x - 1 >= 0:
                color_above = arr[0]
            else:
                color_above = -1

            # Color of the cell to the left (previous column)
            if y - 1 >= 0:
                color_left = arr[-1]
            else:
                color_left = -1

            # Try all 3 colors for current cell
            for c in range(3):
                if c != color_above and c != color_left:

                    # Update state:
                    # - add current color
                    # - drop the oldest color
                    new_arr = [c] + arr[:-1]

                    total += count(conv(new_arr), x + 1, y)

            return total % MOD

        return count(0, 0, 0) % MOD
