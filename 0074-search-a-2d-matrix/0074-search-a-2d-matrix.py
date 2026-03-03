class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Treat the matrix as sorted by rows, where:
        # - Each row is sorted
        # - First element of a row > last element of previous row
        
        rows, cols = len(matrix), len(matrix[0])

        # 1️⃣ Binary search to find the correct row
        top, bot = 0, rows - 1
        while top <= bot:
            row = (top + bot) // 2

            # Target is larger than this row → go down
            if target > matrix[row][-1]:
                top = row + 1

            # Target is smaller than this row → go up
            elif target < matrix[row][0]:
                bot = row - 1

            # Target must be inside this row
            else:
                break

        # If no valid row found
        if not (top <= bot):
            return False

        row = (top + bot) // 2

        # 2️⃣ Binary search inside the selected row
        l, r = 0, cols - 1
        while l <= r:
            m = (l + r) // 2

            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True

        return False