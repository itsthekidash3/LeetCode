class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        R = len(mat)
        C = len(mat[0])

        # rows[i] = total number of 1s in row i
        # cols[j] = total number of 1s in column j
        rows = [0] * R
        cols = [0] * C

        # First pass: count 1s in each row and column
        for i in range(R):
            for j in range(C):
                if mat[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        
        count = 0

        # Second pass: a cell is "special" if it's a 1 AND
        # it's the only 1 in its row AND the only 1 in its column
        for i in range(R):
            for j in range(C):
                if mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    count += 1

        return count