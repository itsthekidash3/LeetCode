class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 1000000007  # Large prime for modulo, to avoid overflow

        # Initial counts for the first row (n = 1)
        # x = patterns with type "ABA" (e.g., 1-2-1)
        # y = patterns with type "ABC" (e.g., 1-2-3)
        # For 3 colors, there are:
        # ABA type: 6 ways (choose first, second color, third same as first)
        # ABC type: 6 ways (choose 3 different colors)
        x, y = 6, 6  

        # Build row by row from 2 to n
        for i in range(2, n + 1):
            # Transition formulas: compute new counts for next row
            # New ABA patterns (new_x):
            # - can come from old ABA in 3 ways
            # - can come from old ABC in 2 ways
            new_x = (3 * x + 2 * y) % MOD

            # New ABC patterns (new_y):
            # - can come from old ABA in 2 ways
            # - can come from old ABC in 2 ways
            new_y = (2 * x + 2 * y) % MOD

            # Update counts for next iteration
            x, y = new_x, new_y

        # Total number of valid colorings for n rows
        return (x + y) % MOD
