class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # Goal: Decode ciphertext by reading diagonals from a row×col matrix
        # Approach: Reconstruct matrix, then read diagonals top-left to bottom-right
        
        N = len(encodedText)  # Total number of characters
        assert(N % rows == 0)  # Ensure text fits perfectly into rows
        cols = N // rows  # Calculate number of columns
        
        # Step 1: Reconstruct the matrix from linear encoded text
        matrix = []
        for i in range(rows):
            # Each row is a slice of cols characters
            matrix.append(encodedText[i * cols : (i + 1) * cols])
        
        ans = []
        
        # Step 2: Read diagonals starting from each column in first row
        for i in range(cols):  # i = starting column for each diagonal
            for j in range(rows):  # j = row index as we traverse diagonal
                # Diagonal moves: row increases by 1, col increases by 1
                # Check if diagonal position (j, i+j) is within bounds
                if j + i < cols:
                    ans.append(matrix[j][i + j])
        
        # Remove trailing spaces (padding from encoding)
        return "".join(ans).rstrip(" ")


    # ========== ALTERNATIVE SOLUTION (WITHOUT EXPLICIT MATRIX) ==========
    # def decodeCiphertext(self, encodedText: str, rows: int) -> str:
    #     # Goal: Decode by reading diagonals without building full matrix
    #     # Approach: Directly compute 1D index for each diagonal position
    #     
    #     # Edge case: single row means no encoding happened
    #     if rows == 1:
    #         return encodedText
    #     
    #     n = len(encodedText)
    #     cols = n // rows
    #     res = []
    #     
    #     # Read each diagonal starting from top row
    #     for c in range(cols):  # c = starting column
    #         r, j = 0, c  # r = row, j = column
    #         
    #         # Traverse diagonal: move down-right (r++, j++)
    #         while r < rows and j < cols:
    #             # Convert 2D position (r, j) to 1D index in encodedText
    #             res.append(encodedText[r * cols + j])
    #             r += 1
    #             j += 1
    #     
    #     # Remove trailing spaces
    #     return "".join(res).rstrip()